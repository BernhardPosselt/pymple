===========================================================
Pymple - A simple Inversion of Control container for Python
===========================================================

.. image:: https://travis-ci.org/owncloud/ocdev.svg
    :target: https://travis-ci.org/owncloud/ocdev

Why
===
If you search for Inversion of Control containers for Python you often encounter the argument "Python is dynamic and does not need those things that static languages need". This is partly true.

Dependency Injection and Inversion of Control is a pattern and not a language feature. It not only makes your code easier to test, but also way more readable. The dependencies are clearly noted in the constructor and your IDEs will give you autocompletion support. If you need to test a class, it is clear where and how to pass in the mocks.

Therefore Inversion and Control and Dependency Injection (which go hand in hand) should also be practiced in dynamic languages. If you think this is not viable, check out `AngularJS <http://angularjs.org/>`_ which also makes use of the above mentioned patterns in a dynamic programming language, namely JavaScript.

For further information watch `Google's Clean Code Talks <https://www.youtube.com/playlist?list=PL693EFD059797C21E>`_

Limitations
===========
Pymple does currently not support:

* Threadsafety
* Lifetimes

Installation
============
This library is a Python 3.2+ library.

Install it via pip for Python 3::

    sudo pip3 install pymple

Usage
=====
Pymple knows three types of parameters:

* Values: A value is simply value that is saved and reused for all other factories/singletons
* Singletons: A singleton is a **callable** that is executed once and the result is saved so future calls to the build method will return the same instance
* Factories: A factory is **callable** that is executed again everytime it is accessed


Registering a value
-------------------

.. code:: python

  from pymple import Container

  container = Container()
  container.value('my_int', 2)

  container.build('my_int') == 2 # True


Registering a Singleton
-----------------------

.. code:: python

  from pymple import Container

  class MyClass:
      def __init__(self, value):
          self.value = value

  container = Container()
  container.value('my_int', 2)
  container.singleton(MyClass, lambda x: MyClass(x.build('my_int')))

  container.build(MyClass) == container.build(MyClass) # True
  container.build(MyClass).value == 2 # True

Registering a Factory
---------------------

.. code:: python

  from pymple import Container

  class MyClass:
      def __init__(self, value):
          self.value = value

  container = Container()
  container.value('my_int', 2)
  container.factory(MyClass, lambda x: MyClass(x.build('my_int')))

  container.build(MyClass) == container.build(MyClass) # False
  container.build(MyClass).value == 2 # True


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
  container.value('param', 3)
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
          self.value('value', 3)
          # etc


  container = Container()
  container.build('value') == 3 # True