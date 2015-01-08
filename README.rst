===========================================================
Pymple - A simple Inversion of Control container for Python
===========================================================

.. image:: https://travis-ci.org/owncloud/ocdev.svg
    :target: https://travis-ci.org/owncloud/ocdev

Installation
============
This library is a Python 3.2 library.

Install it via pip for Python 3::

    sudo pip3 install pymple

Usage
=====
Pymple nows three types of parameters:

* Values: A value is simply value that is saved and reused for all other factories/singletons
* Singletons: A singleton is a **callable** that is executed once and the result is saved so future calls to the build method will return the same instance
* Factories: A factory is **callable** that is executed again everytime it is accessed


.. code:: python

  from pymple.container import Container

  # register simple values
  container.register('param', 2)
  container.build('param') == 2 # True

  # register singletons
  class MyClass:
      def __init__(self, value):
          self.value = value

  container.register_singleton('MyClass', lambda x: MyClass(x.build('param')))
  container.build('MyClass') == container.build('MyClass') # True
  container.build('MyClass').value == 2 # True

  # register factories (no instance will be saved)
  container.register_factory('MyClass', lambda x: MyClass(x.build('param')))
  container.build('MyClass') == container.build('MyClass') # False
  container.build('MyClass').value == 2 # True