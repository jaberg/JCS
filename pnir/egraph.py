"""
An Expression Graph (EGraph) represents a stateless functional relationship
among variables, similar to a block of functional code.

The nodes in an EGraph represent different elements of parsed functional
Python code:
    - variables
    - positional argument bindings
    - keyword argument bindings
    - function bindings

The nodes of an Egraph fall into one of three types:
    - Variable
    - Binding
    - Call

Variable nodes represent values, they point to Bindings when they are used in
expressions. Each expression within an expression graph corresponds to a Call,
and there are edges from Binding nodes to Call nodes.  A Call produces a
single return value (which may be internally structured as a dictionary, list,
array, etc.) but which is represented by a Variable.  Thus we see that
Variables are used by Bindings, Bindings are used by Call nodes, and then Call
nodes are used to define Variables.

"""

import networkx as nx


class Call(object):
    """
    A symbolic expression application
    """


class Variable(object):
    """
    A symbolic value within an expression.

    Edges terminating at this Variable represent computational definitions of
    this Variable.

    Edges beginning at this Variable represent bindings for the purpose of a
    function call.
    """
    def __init__(self, meta=None):
        if meta is None:
            self.meta = {}
        else:
            self.meta = meta

class Binding(object):
    """
    A superclass for various types of bindings, which are roles that Variables
    may play in a function call.  There are three types of Binding:
    - Func - the nature of the function (e.g. add, subtract)
    - PArg - a positional argument to Func
    - KArg - a keyword argument to Func
    """

class FArg(Binding):
    """
    The function / implementation for a Call.
    """


class PArg(Binding):
    """
    A positional argument for a Call.
    """
    def __init__(self, pos):
        self.pos = pos


class KArg(Binding):
    """
    A keyword argument for a Call.
    """
    def __init__(self, kw):
        self.kw = kw



def add_expression(self, etype, inputs, kw_inputs, rval_node=None):

    op_node = Expr(op_type)
    pos_args = [PArg(i) for i, node in enumerate(inputs)]
    kw_args = {kw: KArg(kw) for kw, node in kwinputs.items()}
    if rval_node is None:
        rval_node = Variable()

    # add all nodes in play
    self.add_nodes_from([rval_node, op_node] + pos_args + kw_args.values())

    # add variable -> arg binding edges
    self.add_edges_from(zip(inputs, pos_args))
    self.add_edges_from([(kw_inputs[kw], kw_args[kw])
        for kw in kw_inputs])

    # add arg binding -> expression edges
    self.add_edges_from([(pa, op_node) for pa in pos_args])
    self.add_edges_from([(ka, op_node) for ka in kw_args.values()])

    self.add_edge((op_node, rval_node))

    return rval_node


if 0:
    states = {v: None for v in egraph.variables}
    routines = {'fn': egraph}
