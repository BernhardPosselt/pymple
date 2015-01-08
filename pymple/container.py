import importlib
import inspect

class BuildException(Exception):
    pass

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
        if key in self.registry:
            value = self.registry[key]
            if isinstance(value, Factory):
                value = value(self)
        else:
            # try to create a class
            try:
                # try to separate some.module.klass to some.module and klass
                paths = key.rsplit('.', 1)
                klass = getattr(importlib.import_module(paths[0]), paths[1])
            except ImportError:
                raise BuildException('Could not import class %s' % key)

            if hasattr(klass, '_inject'):
                parameters = {}
                for parameter, value in klass._inject.items():
                    parameters[parameter] = self.build(value)
                value = klass(**parameters)
            else:
                value = klass()
            self.register(key, value)

        return value
