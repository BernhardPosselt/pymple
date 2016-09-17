from unittest import TestCase

from pymple import Container


class A:
    pass


class D(A):
    pass


class B:
    def __init__(self, param: A) -> None:
        self.param = param


class C:
    def __init__(self, param: B) -> None:
        self.param = param


class TestContainer(TestCase):
    def setUp(self) -> None:
        self.container = Container()

    def test_register(self) -> None:
        d = D()
        self.container.register(A, lambda c: d)
        self.assertEqual(d, self.container.resolve(B).param)

    def test_resolve(self) -> None:
        a = self.container.resolve(A)
        self.assertIsInstance(a, A)

        b = self.container.resolve(B)
        self.assertIsInstance(b, B)
        self.assertIsInstance(b.param, A)

    def test_resolve_shared(self) -> None:
        self.container.register(A, lambda c: A(), False)

        a1 = self.container.resolve(A)
        a2 = self.container.resolve(A)
        self.assertIsInstance(a1, A)
        self.assertIsInstance(a2, A)
        self.assertNotEqual(a1, a2)

    def test_alias(self) -> None:
        self.container.alias(A, B)
        a = self.container.resolve(B)
        self.assertIsInstance(a, A)

        c = self.container.resolve(C)
        self.assertIsInstance(c, C)
        self.assertIsInstance(c.param, A)
