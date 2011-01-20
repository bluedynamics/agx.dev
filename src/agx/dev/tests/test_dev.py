# Copyright 2003-2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

import unittest
import doctest
import zope.component
from pprint import pprint
from interlude import interact
from zope.configuration.xmlconfig import XMLConfig

import agx.flavour.dev

optionflags = doctest.NORMALIZE_WHITESPACE | \
              doctest.ELLIPSIS | \
              doctest.REPORT_ONLY_FIRST_FAILURE

TESTFILES = [
    '../confloader.txt',
]

def test_suite():
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', agx.flavour.dev)()
    
    return unittest.TestSuite([
        doctest.DocFileSuite(
            file, 
            optionflags=optionflags,
            globs={'interact': interact,
                   'pprint': pprint},
        ) for file in TESTFILES
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite') 