from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='bb.extjs.core',
      version=version,
      description="Python Framework for ExtJs",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Programming Language :: Python :: 3 :: Only',
          'Natural Language :: English',
          'License :: OSI Approved :: Zope Public License',
          'Operating System :: OS Independent',
          'Development Status :: 4 - Beta'
      ],

      keywords='',
      author='',
      author_email='',
      url='https://github.com/bielbienne/bb.extjs.core',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['bb', 'bb.extjs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'bb.extjs.wsgi',
          'bb.extjs.resources',
          'bb.extjs.scaffolding',
          'bb.extjs.datamanager',
          'bb.extjs.security',
          'bb.extjs.i18n',
          'js.extjs',
          'martian',
          'grokcore.component',
          'zope.interface',
          'Genshi'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
