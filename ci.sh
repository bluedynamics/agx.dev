python --version
python2.6 --version
virtualenv env
python bootstrap.py -c dev.cfg
bin/buildout -c dev.cfg
ls bin/
bin/coverage odict
bin/coverage plumber
bin/coverage node.ext.xml
bin/coverage node.ext.xmi
bin/coverage node.ext.zcml
bin/coverage node.ext.uml
bin/coverage node.ext.python
bin/coverage node.ext.template
bin/coverage node.ext.directory
bin/coverage agx.core
bin/coverage agx.transform.xmi2uml
bin/coverage agx.transform.uml2fs
bin/coverage agx.generator.zca
bin/coverage agx.generator.uml
bin/coverage agx.generator.sql
bin/coverage agx.generator.pyegg
bin/coverage agx.generator.plone
bin/coverage agx.generator.generator
bin/coverage agx.generator.dexterity
bin/coverage agx.generator.buildout
bin/coveragereport