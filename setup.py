import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.0a1'
shortdesc = 'AGX development bundle'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(name='agx.dev',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License (GPL)',
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
