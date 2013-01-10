=======
agx.dev
=======

This is the installation and development buildout for AGX.

This package includes the source checkouts of AGX related packages
(in devsrc/ after having run buildout)
and code for wiring the several available generators together
(see src/agx/dev/confloader.py).

Full documentation is available `here <http://agx.me>`_.


Install
=======

To install AGX for using the generator and possibly for development,
follow the steps from ci.sh, a script we use for continuous integration testing.

.. include:: ci.sh
   ::literal:


Run Tests
=========

You can run tests for a single package, e.g.:

    bin/test agx.generator.pyegg

Or test them all:

   ./test.sh


Changes
=======

1.0 (svn)
---------

  - Initial
