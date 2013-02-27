=======
agx.dev
=======

This is the installation and development buildout for AGX.

This packages includes buildout configurations to use AGX for development, and
to develop AGX itself.

Full documentation is available `here <http://agx.me>`_.


Install for using AGX
---------------------

Run bootstrap.py::

    python bootstrap.py --version 1.7

And buildout::

    ./bin/buildout


Install for developing AGX
--------------------------

Run bootstrap.py::

    python bootstrap.py --version 1.7 -c dev.cfg

And buildout::

    ./bin/buildout -c dev.cfg


Run Tests
---------

You can run tests for a single package, e.g.::

    bin/test agx.generator.pyegg

Or test them all::

   ./test.sh


Issues and Feedback
-------------------

For reporting issues, please use tracker at
``https://github.com/bluedynamics/agx.core/issues``.

For direct feedback or questions send an email to ``dev@agx.me``.


Changes
=======

1.0a1
-----

- Initial Release
