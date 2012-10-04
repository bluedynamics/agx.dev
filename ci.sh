python --version
python2.6 --version
virtualenv env
python bootstrap.py -c dev.cfg
bin/buildout -c dev.cfg
ls bin/
bin/test odict
bin/test plumber
bin/test node.ext.xml
bin/test node.ext.xmi
bin/test node.ext.zcml
bin/test node.ext.uml
bin/test node.ext.python
bin/test node.ext.template
bin/test node.ext.directory
bin/test agx.core
bin/test agx.transform.xmi2uml
bin/test agx.transform.uml2fs
bin/test agx.generator.zca
bin/test agx.generator.uml
bin/test agx.generator.sql
bin/test agx.generator.pyegg
bin/test agx.generator.plone
bin/test agx.generator.generator
bin/test agx.generator.dexterity
bin/test agx.generator.buildout