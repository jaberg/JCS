
import numpy as np
from pnir import from_module

import nnet  # -- ./nnet.py

def test_basic():
    rng = np.random.RandomState(234)

    x = rng.randn(500, 100)
    y = np.sign(rng.randn(500))

    # -- create a function system based on reference implementations
    cpu_nnet = from_module(nnet)

    assert np.all(nnet.w == cpu_nnet.w)

    # -- run each one
    nnet.train_updates(x, y)
    w = nnet.w.copy()

    # -- verify that w's are not aliased
    assert not np.all(w == cpu_nnet.w)
    cpu_nnet.train_updates(x, y)
    assert np.allclose(w, cpu_nnet.w)

    assert np.all(
        np.allclose(
            nnet.predict(x),
            cpu_nnet.predict(x)))


def test_gpu():

    rng = np.random.RandomState(234)

    x = rng.randn(500, 100)
    y = np.sign(rng.randn(500))

    # -- create a function system based on reference implementations
    cpu_mod = from_module(nnet)

    # -- create a function system tuned for GPU evaluation
    gpu_mod = optimize_for_gpu(cpu_mod)

    # -- run each one
    cpu_mod.train_updates(x, y)
    gpu_mod.train_updates(x, y)

    # -- assert that they did about the same thing
    assert np.allclose(cpu_mod.w, gpu_mod.w)
    assert np.allclose(cpu_mod.b, gpu_mod.b)

    # -- serialize the result in a language-agnostic format
    cpu_mod.save('./cpu_mod.tgz')
    gpu_mod.save('./gpu_mod.tgz')

    # -- The saved versions contain the same sort of information as the
    # original nnet.py file: values for w and b, type information, and the
    # mathematics of the functions. It does *not* store whatever optimized
    # compiled code representation was used to implement the function bodies.
    assert open('./cpu_mod.tgz').read() == open('./gpu_mod.tgz').read()

