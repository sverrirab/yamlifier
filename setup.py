from setuptools import find_packages, setup

from os import path

EXCLUDE_FROM_PACKAGES = []

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

requires = []
with open(path.join(here, 'requirements.txt')) as f:
    for l in f.readlines():
        req = l.split('#')[0].strip()
        if req:
            requires.append(req)

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()

setup(
    name='yamlifier',
    version=version,
    url='https://github.com/greenqloud/yamlifier',
    author='Greenqloud',
    description='Utility to create yaml files from a template. Perfect for cloud-config or cloud-init creation.',
    keywords='yaml, cloud-init, cloud-config',
    long_description=long_description,
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    install_requires=requires,
    scripts=[],
    entry_points={'console_scripts': [
        'yamlifier = yamlifier.generate:main',
    ]},
)
