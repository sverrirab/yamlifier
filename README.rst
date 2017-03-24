yamlifier
==============

Utility to create yaml files from a template. Perfect for cloud-config or cloud-init creation.

Create a yaml file from a template and local files.

This allows you to edit files and track in source control and wrap them in yaml files when needed.
Supports compression to minimize yaml size (perfect to squeeze into startup scripts for AWS/EC2 instances).

.. image:: logo.png
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
Use -f to overwrite excisting file and --help for more information.


Template Syntax
---------------

TODO

.. code:: yaml

    # comment that is preserved

    #@ Comments that start with #@ are removed from the output

    #@ You can optionally replace something in the yaml file
    stuff: @@STUFF@@
    script:


Quickstart
----------
See example folder...

.. code:: bash

    yamlifier example.template


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


Background
----------
This was created by `Greenqloud`_ when developing `Qstack`_.

.. _Greenqloud: https://www.greenqloud.com/
.. _Qstack: https://qstack.com/

Hope you find it useful!

Greenqloud Dev Team.