===========================================================
Pymple - A simple Inversion of Control container for Python
===========================================================

.. image:: https://travis-ci.org/owncloud/ocdev.svg
    :target: https://travis-ci.org/owncloud/ocdev

Installation
============
This library is a Python 3 library.

Install it via pip for Python 3:

    sudo pip3 install pymple

Usage
=====

.. code:: python
    from pymple.container import Container

    # register simple values
    container.register('param', 2)
    container.build('param') == 2 # True

    # register singletons
    class MyClass:
        def __init__(self, value):
            self.value = value

    container.register('MyClass', lambda x: MyClass(x.build('param')))
    container.build('MyClass') == container.build('MyClass') # True
    container.build('MyClass').value == 2 # True

    # register factories (no instance will be saved)
    container.register_factory('MyClass', lambda x: MyClass(x.build('param')))
    container.build('MyClass') == container.build('MyClass') # False
    container.build('MyClass').value == 2 # True