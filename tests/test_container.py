import unittest
import sys
from os.path import dirname, abspath

from pymple import inject, Container, BuildException
from pymple.container import Factory

class A:
    pass

class B:
    def __init__(self, b):
        self.b = b

@inject(value1=A, value2='int')
class C:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

class ContainerTest(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_parameter(self):
        self.container.register('Test', 2)
        self.assertEqual(2, self.container.build('Test'))

    def test_register(self):
        self.container.register_singleton('A', lambda x: A())
        self.container.register_singleton('B', lambda x: B(x.build('A')))
        value1 = self.container.build('B')
        value2 = self.container.build('B')
        self.assertTrue(isinstance(value1, B))
        self.assertEqual(value1, value2)
        self.assertEqual(value1.b, value2.b)

    def test_factory(self):
        self.container.register_factory('A', lambda x: A())
        self.container.register_singleton('B', lambda x: B(x.build('A')))
        value1 = self.container.build('B')
        value2 = self.container.build('B')
        self.assertTrue(isinstance(value1, B))
        self.assertEqual(value1, value2)
        self.assertNotEqual(value1.b, self.container.build('A'))

    def test_inject(self):
        # set current path for import to work
        sys.path.append(dirname(abspath(__file__)))
        self.container.register('int', 3)
        self.assertEqual({'value1': A, 'value2': 'int'}, C._inject)
        c = self.container.build(C)
        self.assertEqual(self.container.build(A), c.value1)
        self.assertEqual(3, c.value2)


if __name__ == '__main__':
    unittest.main()