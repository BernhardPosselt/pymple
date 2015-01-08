class Factory:

    def __init__(self, factory):
        self.factory = factory

    def __call__(self, container):
        return self.factory(container)


class Container:

    def __init__(self):
        self.registry = {}

    def register(self, key, value):
        self.registry[key] = value

    def register_factory(self, key, factory):
        self.registry[key] = Factory(factory)

    def build(self, key):
        value = self.registry[key]

        # Check if it is a factory which should not save instances
        # save already instantiate classes
        if isinstance(value, Factory):
            value = value(self)

        elif self._is_lambda(value):
            value = value(self)
            self.registry[key] = value

        return value

    def _is_lambda(self, value):
        lbda = lambda: None
        return isinstance(value, type(lbda)) and \
               value.__name__ == (lbda).__name__