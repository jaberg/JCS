JCS
===

This project is to try out an idea for a new interface for Theano.

Summary
-------

The idea is that "Modules" return as the dominant metaphor for Theano's output,
rather than functions. This is the key thing that will make it possible for
Theano to scale beyond a single device. A module consists of variables (aka
shared variables) and functions, that are jointly optimized for execution on a
particular collection of devices.  Modules are independent in-process servers:
they do not share data or functions.  They are opaque - they implement the
interface of getting and setting module variables and running module functions
but they are at liberty to store internal variables on GPU devices and on remote
computers.


Why is this necessary?
----------------------

The shared variable and function approach requires a global policy on where
shared variables are to be allocated (i.e. a global device flag). This makes it
impossible for Theano to manage multiple devices.


What is to be done?
-------------------

1. To drive home the point that Theano produces Python-style modules, it would
   be great if theano could actually "import" the sort of .py file that Python
   normally imports. That way the semantics and syntax are immediately clear:
   Theano's job is to provide a module with the same interface as the Python
   one.  I've illustrated this with two files in this project: `nnet.py` and
   `train_nnet.py`. The techniques if not code developed for the numba project
   (which I've used for PyAutoDiff) make this quite doable.

2. Define an extensible intermediate representation (IR) to represent the
   interface of such modules: what variables are in a module, what functions,
   and what do those functions do.  This format should be easy to serialize, and
   easy to manipulate.  The Python code representation suggested in (1) is
   serializable, but I would say not easy enough to manipulate.

