import unittest
from pymple.container import Container, Factory

class A:
    pass

class B:
    def __init__(self, b):
        self.b = b

class ContainerTest(unittest.TestCase):

    def setUp(self):
        self.container = Container()

    def test_parameter(self):
        self.container.register('Test', 2)
        self.assertEqual(2, self.container.build('Test'))

    def test_register(self):
        self.container.register('A', lambda x: A())
        self.container.register('B', lambda x: B(x.build('A')))
        value1 = self.container.build('B')
        value2 = self.container.build('B')
        self.assertTrue(isinstance(value1, B))
        self.assertEqual(value1, value2)
        self.assertEqual(value1.b, value2.b)

    def test_factory(self):
        self.container.register_factory('A', lambda x: A())
        self.container.register('B', lambda x: B(x.build('A')))
        value1 = self.container.build('B')
        value2 = self.container.build('B')
        self.assertTrue(isinstance(value1, B))
        self.assertEqual(value1, value2)
        self.assertNotEqual(value1.b, self.container.build('A'))

    def test_is_lambda(self):
        def a():
            pass
        self.assertTrue(self.container._is_lambda(lambda x: x))
        self.assertFalse(self.container._is_lambda(a))

if __name__ == '__main__':
    unittest.main()