===========================================================
Pymple - A simple Inversion of Control container for Python
===========================================================

Required: Python 3

Usage
=====

.. code-block:: python
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