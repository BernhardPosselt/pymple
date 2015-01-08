===========================================================
Pymple - A simple Inversion of Control container for Python
===========================================================

.. image:: https://travis-ci.org/owncloud/ocdev.svg
    :target: https://travis-ci.org/owncloud/ocdev

Installation
============
This library is a Python 3.2+ library.

Install it via pip for Python 3::

    sudo pip3 install pymple

Usage
=====
Pymple nows three types of parameters:

* Values: A value is simply value that is saved and reused for all other factories/singletons
* Singletons: A singleton is a **callable** that is executed once and the result is saved so future calls to the build method will return the same instance
* Factories: A factory is **callable** that is executed again everytime it is accessed


.. code:: python

  from pymple import Container

  # register simple values
  container.register('value', 2)
  container.build('value') == 2 # True

  # register singletons
  class MyClass:

      def __init__(self, value):
          self.value = value


  container.register_singleton('MyClass', lambda x: MyClass(x.build('value')))
  container.build('MyClass') == container.build('MyClass') # True
  container.build('MyClass').value == 2 # True

  # register factories (no instance will be saved)
  container.register_factory('MyClass', lambda x: MyClass(x.build('value')))
  container.build('MyClass') == container.build('MyClass') # False
  container.build('MyClass').value == 2 # True

Using the @inject decorator
===========================
Instead of registering all values in the container, you can try to let the container assemble the class automatically

.. code:: python

  from pymple import Container

  class A:
      pass

  container = Container()
  a = container.build(A)

  isinstance(a, A) # True


This works if the constructor is empty. If the constructor is not empty, the container needs a map from parameter value to container value as a static **_inject** attribute on the class. This attribute can be set with the **@inject** decorator:

.. code:: python

  from pymple import inject, Container
  from some.module import A

  @inject(value=A, value2='param')
  class C:

      def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

  container = Container()
  container.register('param', 3)
  c = container.build(C)

  isinstance(c.value, A) # True
  c.value2 == 3 # True


Extending the container
=======================
You can also extend the container to make it reusable:

.. code:: python

  from pymple.container import Container

  class MyContainer(Container):

      def __init(self):
          super().__init__()
          self.register('value', 3)


  container = MyContainer()
  container.build('value') == 3 # True