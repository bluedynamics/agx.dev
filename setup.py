# Copyright 2003-2009, BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2
import os
from setuptools import (
    setup,
    find_packages,
)


version = 'dev'
shortdesc = 'AGX development Bundle.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='agx.dev',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python', 
      ],
      keywords='AGX, Code Generator',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://github.com/bluedynamics/agx.dev',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['agx'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'agx.generator.uml',
          'agx.generator.dexterity',
          'agx.generator.sql',
          #'agx.generator.cornice',
          'agx.generator.generator',
      ],
      extras_require = dict(
          test=[
              'interlude',
          ]
      ),
      entry_points={
          'console_scripts': [
              'agx = agx.dev.main:run',
          ],
      })
