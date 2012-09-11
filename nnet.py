"""
Dual-purpose file that is

a) an importable Python module, and

b) a standalone function-system description for theano.load_py

"""

import numpy as np
from contracts import contract
from autodiff import grad

w = np.random.rand(100)
b = np.random.rand()
lr = 0.001

__contract_w = 'array[100](float64)'
__contract_b = 'float'
__contract_lr = 'float'

x_spec = 'array[Mx100](float64)'
y_spec = 'array[M](int,(-1|1))'


@contract(x=x_spec, y=y_spec)
def train_update(x, y):
    global w, b
    err = np.sum((y - (np.dot(x, w) + b)) ** 2)
    gw, gb = grad(err, [w, b])
    w -= lr * gw
    b -= lr * gb


@contract(x=x_spec)
def predict(x):
    return np.sign(np.dot(x, w) + b)

