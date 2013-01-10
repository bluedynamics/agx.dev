# Copyright 2003-2013, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2
from zope.configuration.xmlconfig import XMLConfig
import agx.core
import agx.core.main


def run():
    """
    ./bin/agx dev/agx.transform.xmi2uml/referencemodels/examplegg.uml
    -p dev/agx.transform.xmi2uml/referencemodels/pyegg.profile.uml
    -o /opt/agxtest/
    """
    XMLConfig('configure.zcml', agx.core)()
    agx.core.main.run()
