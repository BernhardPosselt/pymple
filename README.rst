===========================================================
Pymple - A Simple Inversion of Control Container For Python
===========================================================

.. image:: https://travis-ci.org/BernhardPosselt/pymple.svg?branch=master
    :target: https://travis-ci.org/BernhardPosselt/pymple

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
This library is a Python 3.4+ library. On Python 3.4 however the **typings** package is required.

Install it via pip for Python 3::

    sudo pip3 install pymple

Usage
=====
Pymple knows two types of parameters:

* Singletons: A singleton is a **callable** that is executed once and the result is saved so future calls to the build method will return the same instance
* Factories: A factory is **callable** that is executed again every time it is accessed

By default Pymple tries to resolved a singleton based on the annotated type, e.g.:

.. code:: python

  from pymple import Container

  class A:
      def __init__(self):
          pass

  class B:
      def __init__(self, param: A):
          self.a = A

  container = Container()
  b = container.resolve(B)
  isinstance(b.a, A) == True

# Overriding The Default Behavior
However you can also override it by defining it explicitly:

.. code:: python

  container = Container()
  ccontainer.register(B, lambda c: B('hi'))

  b = container.resolve(B)
  b.a == 'hi'

The first passed in variable to the lambda is the container instance itself, so you can also resolve other classes on it:

.. code:: python

  container = Container()
  ccontainer.register(B, lambda c: B(c.resolve(A)))

  b = container.resolve(B)
  isinstance(b.a, A) == True

# Registering Factories
If you want to register a factory instead of a singleton, simple pass False as the second parameter:

.. code:: python

  container = Container()
  ccontainer.register(B, lambda c: B('hi'), False)

  b = container.resolve(B)
  c = container.resolve(B)
  b != c

# Aliasing
Sometimes a type interface uses an abstract class as type annotation. In that case you can simply define an alias:

.. code:: python

  container = Container()
  ccontainer.alias(ConcreteClass, AbstractClass)

  clazz = container.resolve(AbstractClass)
  isinstance(clazz, ConcreteClass) == True

