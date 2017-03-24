#!/bin/bash

set -e

ARCHIVE="/example/archive.tgz"
MSG="@@VARIABLE1@@"

function extract {
    if [ -f $1 ] ; then
        echo "Extracting $1"
        tar xf $1 -C $2
        rm -f $1
    fi
}

mkdir -p /example/output

extract ${ARCHIVE} /example/output

echo "Hello ${MSG} - installing..."

# Continue installation using files from package...

ls -al /example
