from functools import partial
import numpy as np

from pnir.module import ModuleFactory
from pnir.module import property_any
from pnir.module import property_numpy


class method_double_into(property):

    def __init__(self, vin, vout):
        self.vin = vin
        self.vout = vout
        property.__init__(self)

    def __get__(self, mod, cls):
        return partial(self, mod=mod)

    def __call__(self, mod):
        tmp = mod.states[self.vin] * 2
        mod.states[self.vout] = tmp


def test_basic():
    m = ModuleFactory()

    # explicit construction is meant to be possible, but
    # not always the best way to create modules.
    m.add_attr('a', property_any('avar'))
    m.add_attr('b', property_numpy('bvar'))
    m.add_method('c', method_double_into('bvar', 'avar'))

    m.a = 1
    m.b = 1

    assert type(m.states['avar']) == int
    assert type(m.states['bvar']) == np.ndarray

    assert type(m.a) == int
    assert type(m.b) == np.ndarray

    assert m.a == 1
    assert m.b == 1

    assert len(m.states) == 2

    m.c()
    assert m.a == 2
    assert m.b == 1
    assert len(m.states) == 2
