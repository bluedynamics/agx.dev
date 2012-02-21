# Copyright 2003-2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

import os
from zope.interface import implements
from zope.configuration.xmlconfig import XMLConfig
from agx.core.interfaces import IConfLoader
import agx.generator.uml
import agx.generator.pyegg
import agx.generator.zca
import agx.generator.plone
import agx.generator.dexterity
import agx.generator.buildout

class ConfLoader(object):
    
    implements(IConfLoader)
    
    flavour = 'Develop'
    
    transforms = [
        'xmi2uml',
        'uml2fs',
    ]
    
    @property
    def profiles(self):
        ret = list()
        for module in [agx.generator.pyegg,
                       agx.generator.zca,
                       agx.generator.plone,
                       agx.generator.dexterity,
                       agx.generator.buildout]:
            for profile in self._profiles(module):
                ret.append(profile)
        return ret
    
    def _profiles(self, module):
        basepath = os.path.split(module.__file__)[:-1][0]
        profilepath = os.path.join(basepath, 'profiles')
        ret = list()
        if os.path.exists(profilepath) and os.path.isdir(profilepath):
            for file in os.listdir(profilepath):
                if file.endswith('uml'):
                    ret.append([
                        file[0:file.find('.profile.uml')],
                        os.path.join(profilepath, file),
                    ])
        return ret
    
    def __call__(self):
        XMLConfig('configure.zcml', agx.generator.uml)()
        XMLConfig('configure.zcml', agx.generator.pyegg)()
        XMLConfig('configure.zcml', agx.generator.zca)()
        XMLConfig('configure.zcml', agx.generator.plone)()
        XMLConfig('configure.zcml', agx.generator.dexterity)()
        XMLConfig('configure.zcml', agx.generator.buildout)()