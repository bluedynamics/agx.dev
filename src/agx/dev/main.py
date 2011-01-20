# Copyright 2003-2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from zope.configuration.xmlconfig import XMLConfig
import agx.core.main
import agx.flavour.dev

def run():
    """
    ./bin/agx dev/agx.transform.xmi2uml/referencemodels/examplegg.uml 
    -p dev/agx.transform.xmi2uml/referencemodels/pyegg.profile.uml 
    -o /opt/agxtest/
    """
    XMLConfig('configure.zcml', agx.flavour.dev)()
    agx.core.main.run()