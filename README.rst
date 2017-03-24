yamlifier
==============

Utility to create yaml files from a template. Perfect for cloud-config or cloud-init creation.

Create a yaml file from a template and local files.

This allows you to edit files and track in source control and wrap them in yaml files when needed.
Supports compression to minimize yaml size (perfect to squeeze into startup scripts for AWS/EC2 instances).

.. image:: logo.png
    :alt: File graphic by href="http://www.flaticon.com/authors/freepik - made by http://logomakr.com

Installation
------------

.. code:: bash

    pip install yamlifier


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

    docker

File graphic by <a href="http://www.flaticon.com/authors/freepik">Freepik</a> from <a href="http://www.flaticon.com/">Flaticon</a> is licensed under <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC BY 3.0</a>. Made with <a href="http://logomakr.com" title="Logo Maker">Logo Maker</a>

Credits
-------

Logo
Background
----------
This was created by `Greenqloud`_ when developing `Qstack`_.

.. _Greenqloud: https://www.greenqloud.com/
.. _Qstack: https://qstack.com/

Hope you find it useful!

Greenqloud Dev Team.