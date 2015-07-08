.. image:: https://travis-ci.org/bielbienne/bst.pygasus.demo.svg?branch=master
    :target: https://travis-ci.org/bielbienne/bst.pygasus.demo

.. contents::

Introduction
============

Pygasus is a new Python 3 framework to build web applications with
`Sencha ExtJS <https://www.sencha.com/products/extjs/#overview>`_. Pygasus is designed to be full
customizable for your project. 

bst.pygasus and all corresponding submodules are licensed under the ZPL 2.1, see LICENSE.txt for details.

Architecture
------------

.. figure:: docs/architecture.png
   :alt: Architecture

   yellow modules are planned to be developed in the near future

The various packages are:

bst.extjs.core
    The core package of the framework that assembles all required packages together.

bst.extjs.datamanager
    The datamanager manages data coming from the client and data sent to the client's browser.

bst.extjs.i18n
    This package handles the translation for multilingual sites and applications.

bst.extjs.scaffolding
    Scaffolding is a package to generate standard models, stores, views and grids for ExtJs. 

bst.extjs.security
    This package provide a default login mask and a pluggable authentication. In the future we also plan to
    implement a role based permission model.

bst.extjs.session
    This package creates a cookie on client browsers and provides a server side session store.

bst.extjs.wsgi
    The layer needed to let the application work as a WSGI server.

bst.extjs.resources
    This package is responsible to share all needed static resources with the client.


Getting started
===============

Recommendation
--------------

The ZCA (Zope component Architectur) is a main element in this framework. If you are not familiar with it, we recommend you first learn its basics. You can follow the links at the bottom of this page.

Buildout
--------

We recommend to setup up a buildout for your project. First It will install all required dependencies and the scripts needed to run a server. The boostrap file can be downloaded at https://bootstrap.pypa.io/bootstrap-buildout.py.

File structure:

.. code::

    buildout
    ├── bootstrap.py
    ├── buildout.cfg
    ├── etc
    │   ├── deploy.ini.in
    │   └── site.zcml.in
    └── dev
        └── myproject

buildout.cfg

.. code:: ini

    [buildout]
    
    extends = 
        https://raw.githubusercontent.com/bielbienne/bst.pygasus.demo/master/sources.cfg
        https://raw.githubusercontent.com/bielbienne/bst.pygasus.demo/master/versions.cfg
    
    develop = dev/myproject  
    parts =
        app
        zcml
    
    extensions = mr.developer
    auto-checkout =
        js.extjs
        bst.pygasus.core
        bst.pygasus.wsgi
        bst.pygasus.scaffolding
        bst.pygasus.datamanager
        bst.pygasus.resources
        bst.pygasus.security
        bst.pygasus.session
        bst.pygasus.i18n
        bst.pygasus.demo
    
    [debug_ini]
    recipe = collective.recipe.template
    input = etc/deploy.ini.in
    output = ${buildout:parts-directory}/etc/${:outfile}
    outfile = debug.ini
    
    [zcml]
    recipe = collective.recipe.template
    input = etc/site.zcml.in
    output = ${buildout:parts-directory}/etc/${:outfile}
    outfile = site.zcml
    
    [app]
    recipe = zc.recipe.egg:script
    arguments="${debug_ini:output}"
    eggs =
        bst.pygasus.wsgi
        myproject

etc/deploy.ini.in

.. code:: ini

    [zcml]
    path = ${zcml:output}

    [app:main]
    use = egg:bst.pygasus.wsgi#main

    [server:debug]
    use = egg:waitress#http
    host = 127.0.0.1
    port = 5000
    threadpool_workers = 1
    threadpool_spawn_if_under = 1
    threadpool_max_requests = 0

etc/site.zcml.in

.. code:: xml

    <configure xmlns="http://namespaces.zope.org/zope">
        <include package="myproject" />
    </configure>

Run your buildout. (You must first create your own project, show next part)

.. code:: bash

    $ cd buildout
    $ python3 boostrap.py
    $ ./bin/buildout


Create an application
---------------------

Proposed File Structure
~~~~~~~~~~~~~~~~~~~~~~~

setup configure.zcml
~~~~~~~~~~~~~~~~~~~~

.. code:: xml

    <configure xmlns="http://namespaces.zope.org/zope"
               xmlns:grok="http://namespaces.zope.org/grok"
               xmlns:i18n="http://namespaces.zope.org/i18n"
               i18n_domain="myproject">
    
        <include package="bst.pygasus.core" />
    
        <grok:grok package="." />
    
        <i18n:registerTranslations directory="locales" />
    
    </configure>


Create an application context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from fanstatic import Library
    from fanstatic import Resource
    from bst.pygasus.core import ext
        
    library = Library('demo', 'app')

    class DemoContext(ext.ApplicationContext):
    
        title = 'Demo'
        application = 'bst.pygasus.demo.Application'
        namespace = 'bst.pygasus.demo'
        resources = Resource(library, 'application.js',
                             depends=[ext.extjs_resources])

Register additional ExtJs paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    class ViewClassPathMapping(ext.ClassPathMapping):
        namespace = 'bst.pygasus.demo.view'
        path = 'fanstatic/demo/view'

Define a schema
~~~~~~~~~~~~~~~

.. code:: python

    from bst.pygasus.core import ext
        
    from zope import schema
    from zope.interface import Interface
    
    @ext.scaffolding('Card', 'Magic the Gathering')
    class ICard(Interface):
        id = schema.Id(title='ID', required=False)
    
        name = schema.TextLine(title='Name', required=True)

        costs = schema.Int(title='Costs', required=False)

        publication = schema.Date(title='Publication', required=True)


Create a Model
~~~~~~~~~~~~~~

.. code:: python

    from bst.pygasus.core import ext
    from bst.pygasus.demo import schema
    from zope.schema.fieldproperty import FieldProperty

    class Card(ext.Model):
        ext.schema(schema.ICard)
        id = FieldProperty(ICard['id'])
        name = FieldProperty(ICard['name'])
        costs = FieldProperty(ICard['costs'])
        publication = FieldProperty(ICard['publication'])

Create a handler for CRUD requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

i18n (Internationalization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~



Demo application
----------------
We have a demo application that you can easy install with a buildout file. If you are interested, please follow the instruction at `bst.pygasus.demo <https://github.com/bielbienne/bst.pygasus.demo>`_..


Additional References
=====================

* http://zopeinterface.readthedocs.org/en/latest/
* http://zopecomponent.readthedocs.org/en/latest/
* https://www.python.org/dev/peps/pep-0333/
* https://pypi.python.org/pypi/martian
* https://pypi.python.org/pypi/zc.buildout/2.4.0
* http://grok.zope.org/documentation/tutorial/grok-poller-tutorial/adapters
* http://www.fanstatic.org/en/latest/


About us
========
We are the IT Services of Biel/Bienne, Switzerland.
http://foss.biel-bienne.ch/blog/
