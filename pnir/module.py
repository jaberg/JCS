import numpy as np


class property_any(property):

    def __init__(self, variable):
        self.variable = variable
        property.__init__(self)

    def __get__(self, mod, cls):
        return mod.states[self.variable]

    def __set__(self, mod, value):
        mod.states[self.variable] = self(value)

    def __call__(self, value):
        return value


class property_numpy(property):

    def __init__(self, variable):
        self.variable = variable
        property.__init__(self)

    def __get__(self, mod, cls):
        return mod.states[self.variable]

    def __set__(self, mod, value):
        mod.states[self.variable] = self(value)

    def __call__(self, value):
        return np.asarray(value)


def ModuleFactory(*args, **kwargs):
    class Module_(object):
        def __init__(self, *args, **kwargs):
            self.states = {}
            self.routines = {}

        @classmethod
        def add_attr(cls, attr, prop):
            setattr(cls, attr, prop)

        @classmethod
        def add_method(cls, attr, prop):
            setattr(cls, attr, prop)

    Module_.__name__ = 'Module'
    return Module_()


