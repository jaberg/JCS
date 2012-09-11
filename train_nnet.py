"""
Sample code for what is being *PROPOSED* for a new Theano module interface.

It does not currently work.
"""
import numpy as np
from theano import load_py

rng = np.random.RandomState(234)

x = rng.randn(500, 100)
y = np.sign(rng.randn(500))

# -- create a function system based on reference implementations
cpu_mod = theano.load_py('./nnet.py', device='cpu', optimizer=None)

# -- create a function system tuned for GPU evaluation
gpu_mod = theano.load_py('./nnet.py', device='gpu0')

# -- run each one
cpu_mod.train_updates(x, y)
gpu_mod.train_updates(x, y)

# -- assert that they did about the same thing
assert np.allclose(cpu_mod.w, gpu_mod.w)
assert np.allclose(cpu_mod.b, gpu_mod.b)

# -- serialize the result in a language-agnostic format
cpu_mod.save('./cpu_mod.tgz')
gpu_mod.save('./gpu_mod.tgz')

# -- The saved versions contain the same sort of information as the original
#    nnet.py file: values for w and b, type information, and the mathematics
#    of the functions. It does *not* store whatever optimized compiled code
#    representation was used to implement the function bodies.
assert open('./cpu_mod.tgz').read() == open('./gpu_mod.tgz').read()

