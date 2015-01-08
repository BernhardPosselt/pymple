class Factory:

    def __init__(self, factory):
        self.factory = factory

    def __call__(self, container):
        return self.factory(container)


class Singleton(Factory):

    def __init__(self, factory):
        super().__init__(factory)
        self.value = None

    def __call__(self, container):
        if self.value == None:
            self.value = super().__call__(container)
        return self.value


class Container:

    def __init__(self):
        self.registry = {}

    def register(self, key, value):
        self.registry[key] = value

    def register_factory(self, key, factory):
        self.registry[key] = Factory(factory)

    def register_singleton(self, key, factory):
        self.registry[key] = Singleton(factory)

    def build(self, key):
        value = self.registry[key]

        # Check if it is a factory which should not save instances
        # save already instantiate classes
        if isinstance(value, Factory):
            value = value(self)

        return value
