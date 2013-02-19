echo "==================== running the tests ===================="

echo "-------------------- bin/test odict -----------------------"
bin/test odict
echo "-------------------- bin/test plumber  --------------------"
bin/test plumber
echo "-------------------- bin/test node.ext.xml ----------------"
bin/test node.ext.xml
echo "-------------------- bin/test node.ext.xmi ----------------"
bin/test node.ext.xmi
echo "-------------------- bin/test node.ext.zcml ---------------"
bin/test node.ext.zcml
echo "-------------------- bin/test node.ext.uml ----------------"
bin/test node.ext.uml
echo "-------------------- bin/test node.ext.python -------------"
bin/test node.ext.python
echo "-------------------- bin/test node.ext.template -----------"
bin/test node.ext.template
echo "-------------------- bin/test node.ext.directory ----------"
bin/test node.ext.directory
echo "-------------------- bin/test agx.core --------------------"
bin/test agx.core
echo "-------------------- bin/test agx.transform.xmi2uml -------"
bin/test agx.transform.xmi2uml
echo "-------------------- bin/test agx.transform.uml2fs --------"
bin/test agx.transform.uml2fs
echo "-------------------- bin/test agx.generator.zca -----------"
bin/test agx.generator.zca
echo "-------------------- bin/test agx.generator.uml -----------"
bin/test agx.generator.uml
echo "-------------------- bin/test agx.generator.sql -----------"
bin/test agx.generator.sql
echo "-------------------- bin/test agx.generator.pyegg ---------"
bin/test agx.generator.pyegg
echo "-------------------- bin/test agx.generator.plone ---------"
bin/test agx.generator.plone
echo "-------------------- bin/test agx.generator.generator -----"
bin/test agx.generator.generator
echo "-------------------- bin/test agx.generator.dexterity -----"
bin/test agx.generator.dexterity
echo "-------------------- bin/test agx.generator.buildout ------"
bin/test agx.generator.buildout
#echo "-------------------- bin/test agx.generator.cornice -------"
#bin/test agx.generator.cornice
echo "==================== ran all the tests ===================="