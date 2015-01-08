from pymple.container import Container, BuildException

def inject(**kwargs):
    def injector(klass):
        # handle inheritance
        if hasattr(klass, '_inject'):
            for key, value in kwargs.items():
                klass._inject[key] = value
        else:
            klass._inject = kwargs
        return klass

    return injector