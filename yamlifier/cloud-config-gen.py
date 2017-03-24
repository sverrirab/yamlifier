#!/usr/bin/env python

from __future__ import print_function

import argparse
import functools
import os
import re
import tarfile
import tempfile

import ruamel.yaml

MAX_OUTPUT_SIZE = 24 * 1024

ERR_SUCCESS = 0
ERR_NOT_FOUND = 1
ERR_ALREADY_EXISTS = 2
ERR_FILE_TOO_LARGE = 3

LOCAL_CONTENT_PATH = "local-content-path"
LOCAL_CONTENT_TAR_PATH = "local-content-tar-path"

VERBOSE = 0


def read_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read(), ERR_SUCCESS
    print("File", path, "not found")
    return "", ERR_NOT_FOUND


# Function that fixes file permissions in a tar.
def tarinfo_filter(owner, permissions, tarinfo):
    if owner == "root":
        tarinfo.uid = tarinfo.gid = 0
        tarinfo.uname = tarinfo.gname = owner
    elif owner:
        # we don't know the uid/gid - should we assume gname == uname?
        tarinfo.uname = owner

    if permissions:
        # Note: this will replace permissions on files and folders
        # Possibly add support for adding executable bit to folders?
        old_perm = int(permissions, 8)
        new_mode = (tarinfo.mode & int("7777000", 8)) | old_perm
        tarinfo.mode = new_mode
    return tarinfo


def main(args, subst):
    template, err = read_file(args.template)
    if err:
        return err

    code = ruamel.yaml.load(template, ruamel.yaml.RoundTripLoader)
    for f in code.get("write_files"):
        if LOCAL_CONTENT_PATH in f:
            path = os.path.join(args.content_root, f.get(LOCAL_CONTENT_PATH))
            content, err = read_file(path)
            if err:
                return err

            del f[LOCAL_CONTENT_PATH]
            f["content"] = ruamel.yaml.scalarstring.PreservedScalarString(content)

        elif LOCAL_CONTENT_TAR_PATH in f:
            owner = f.get("owner", "")
            permissions = f.get("permissions", "")
            path = os.path.join(args.content_root, f.get(LOCAL_CONTENT_TAR_PATH))
            _, tgz_path = tempfile.mkstemp(".tgz")
            tgz = tarfile.open(tgz_path, "w:gz")
            tgz.add(path,
                    arcname=".",
                    recursive=True,
                    filter=functools.partial(tarinfo_filter, owner, permissions))
            tgz.close()
            with open(tgz_path, "rb") as tgz_file:
                tgz_content = tgz_file.read()
            os.unlink(tgz_path)

            del f[LOCAL_CONTENT_TAR_PATH]
            f["content"] = tgz_content

    if os.path.exists(args.output) and not args.force:
        print("Output file already exists.  Remove or specify --force")
        return ERR_ALREADY_EXISTS

    output = ruamel.yaml.dump(code, Dumper=ruamel.yaml.RoundTripDumper)

    # Remove comments
    output = re.sub("\s*#@\s.*$", "", output, flags=re.MULTILINE)

    # Substitutions
    for s in sorted(subst.keys()):
        output = output.replace("@@" + s + "@@", subst[s])

    # Check size
    if (not args.large) and (len(output) > MAX_OUTPUT_SIZE):
        print("Output file too large!")
        return ERR_FILE_TOO_LARGE

    with open(args.output, "w") as f:
        f.write(output)

    print("Generated", args.output, "successfully.")
    return ERR_SUCCESS


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generate cloud-config.yaml")

    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Increase output verbosity")
    parser.add_argument("-c", "--content-root", default=".",
                        help="Root folder for local-content-path files")
    parser.add_argument("-t", "--template", default="cloud-config-template.yaml",
                        help="Template file to read")
    parser.add_argument("-o", "--output", default="cloud-config.yaml",
                        help="Output file to write to")
    parser.add_argument("-f", "--force", default=False, action="store_true",
                        help="Overwrite output file even if exists")
    parser.add_argument("-xl", "--large", default=False, action="store_true",
                        help="Allow large (>24Kb) template output")
    parser.add_argument("substitution", nargs="*",
                        help="key=value pairs for @@KEY@@ substitutions")

    parsed_args = parser.parse_args()

    VERBOSE = parsed_args.verbose

    subst = {}
    for s in parsed_args.substitution:
        split = s.split("=", 1)
        if len(split) < 2 or not split[0].isupper():
            parser.error("substitution \"{}\" format error - correct is: \"UPPERCASE=some value\"".format(s))
            exit(1)
        subst[split[0]] = split[1]

    if VERBOSE:
        for k in sorted(subst.keys()):
            print("substituting {}=\"{}\"".format(k, subst[k]))

    exit(main(parsed_args, subst))
