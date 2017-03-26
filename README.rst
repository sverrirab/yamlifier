yamlifier
==============

Create a yaml file from a template and automatically embed local files.

Create builds for your cloud-init / cloud-config templates with ease!

This allows you to edit files and track in source control and wrap them in yaml files when needed.
Supports compression to minimize yaml size (perfect to squeeze into startup scripts for AWS/EC2 instances).

.. image:: https://github.com/greenqloud/yamlifier/raw/master/logo.png
    :width: 200px
    :align: center
    :alt: File graphic by href="http://www.flaticon.com/authors/freepik - made by http://logomakr.com

Getting started
---------------

.. code:: bash

    pip install yamlifier

    cd testdata

    yamlifier VARIABLE1="funny person"


Check out the generated.yaml file in the local folder.
Use -f to overwrite existing file and --help for more information.


Template Syntax
---------------

.. code:: yaml

    #cloud-config
    #@ Comments like this will be removed from the generated file.
    runcmd:
      - [ /example/install.sh ]

    write_files:
      #@ 'local-content-path' will be replaced with content of local file.
      - path: /example/install.sh
        permissions: "0755"
        owner: "root"
        local-content-path: example_files/install.sh

      #@ Embed binary file as an example (could be an executable)
      - path: /example/small_logo.png
        permissions: "644"
        owner: "root"
        local-content-path: example_files/small_logo.png

      #@ Embed archive with multiple small files
      #@ 'local-content-tar-path' will be replaced with an embedded archive with all files in folder.
      - path: /example/archive.tgz
        permissions: "644"
        owner: "root"
        local-content-tar-path: example_files/subfolder


Building & Testing using Docker
-------------------------------

Check out the git repository and from the yamlifier folder:

.. code:: bash

    docker build -t yamlifier2 -f docker/python2.Dockerfile .

    docker run -it -v $PWD:/code yamlifier2 bash


Credits
-------

Based on the excellent `ruamel.yaml`_ library that allows manipulating yaml files while preserving comments and order.

.. _ruamel.yaml: https://pypi.python.org/pypi/ruamel.yaml

Logo created with `logomakr.com`_ (image CC BY 3.0 license).

.. _logomakr.com: http://logomakr.com


Source code and feedback
------------------------

Fully open sourced with `Apache License`_ on `github.com/greenqloud/yamlifier`_ including issue tracking.

.. _Apache License: https://github.com/greenqloud/yamlifier/blob/master/LICENSE.rst
.. _github.com/greenqloud/yamlifier: https://github.com/greenqloud/yamlifier


Background
----------
This was created by `Greenqloud`_ when developing `Qstack`_.

.. _Greenqloud: https://www.greenqloud.com/
.. _Qstack: https://qstack.com/

Hope you find it useful!

Greenqloud Dev Team.
