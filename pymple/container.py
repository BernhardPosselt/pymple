class BuildException(Exception):
    pass

class Factory:

    def __init__(self, factory):
        self.factory = factory

    def __call__(self, container):
        return self.factory(container)


class Singleton(Factory):
    pass


class Container:

    def __init__(self):
        self._factories = {}
        self._values = {}


    def value(self, key, val):
        self._values[key] = val


    def factory(self, key, factory):
        self._factories[key] = Factory(factory)


    def singleton(self, key, factory):
        self._factories[key] = Singleton(factory)


    def build(self, key):
        # if a value is already saved return it
        if key in self._values:
            value = self._values[key]

        # if no value is saved, construct it
        elif key in self._factories:
            factory = self._factories[key]
            value = factory(self)

            # save singleton instances
            if isinstance(factory, Singleton):
                self._values[key] = value

        # finally if no factory is registered, create an instance if possible
        else:
            if hasattr(key, '_inject'):
                parameters = {}
                for parameter, value in key._inject.items():
                    parameters[parameter] = self.build(value)
                value = key(**parameters)
            else:
                try:
                    value = key()
                except TypeError as e:
                    msg = (('%s is neither a class nor function or does not '
                          'receive all required parameters: %s') % (key, e))
                    raise BuildException(msg)

            self.value(key, value)

        return value
