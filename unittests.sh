#!/bin/bash

# create a virtual python environment separated from the system python
#virtualenv .
# install nose and coverage into it
#bin/pip install nose coverage
# rerun buildout, so we get a working /bin/pyagx
#bin/buildout -c dev.cfg
#
# there are two options
# 1) run the tests by calling the test_foo.py files
#    - bad: have to call them all separately
#    - bad: no relevant output other than on the console output
#
# examples:
#
# bin/pyagx devsrc/node.ext.python/src/node/ext/python/tests/test_goparser.py
# bin/pyagx devsrc/node.ext.python/src/node/ext/python/tests/test_gonodes.py
#
# 2) have tests discovered and run by nose
#    - bad: sys.path stanza (with all the agx and node packages)
#           needs to be transplanted from bin/pyagx to bin/nosetests
#           can this be done with buildout?
#
#           gogo says: we need to add 'nose' and 'coverage'. 
#
echo "====================================================================="
echo "you need to copy sys.path[0:0] = [...] from bin/agx to bin/nosetests."
echo "otherwise nose wont work, I'm afraid."
echo "you also need to switch to branch artsprint2013 in node.ext.python"
echo "because that is where the unittests are."
echo "====================================================================="
#    - good: less files to call
#    - good: coverage is easily done
#    - good: coverage can produce output of several forms:
#            - .coverage
#            - html
#            - xml/xunit (for fancy display in jenkins: xml-output)
#
# examples:
#
# bin/nosetests devsrc/node.ext.python/src/node/ext/python/ --with-coverage
#    - good: coverage can be restricted to a certain package
bin/nosetests devsrc/node.ext.directory/src/node/ext/directory/ --with-coverage --cover-package=node.ext.directory
#    - good: while writing tests, you can choose to run specific tests only
# bin/nosetests devsrc/node.ext.python/src/node/ext/python/tests/test_goparser.py:TestMetanode.test_handle_upside_down_ness --with-coverage --cover-package=node.ext.python
#
#
#
echo "done."
