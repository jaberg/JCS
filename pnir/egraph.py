import networkx as nx


class Expression(object):
    def __init__(self, etype):
        self.etype = etype


class Binding(object):
    pass


class Variable(object):
    def __init__(self, meta=None):
        if meta is None:
            self.meta = {}
        else:
            self.meta = meta


class PArg(Binding):
    def __init__(self, pos):
        self.pos = pos


class KArg(Binding):
    def __init__(self, kw):
        self.kw = kw


class EGraph(nx.DiGraph):
    """

    An expression graph (ExprGraph) is a directed graph with paths of the
    form:

    ```
    variable -> arg binding -> expression -> variable
    ```

    The nodes are typed as follows:

    * `variable` nodes: `Variable`

    * `arg binding` nodes: `Binding` subclass `KArg` or `PArg`

    * `expression` nodes: `Expression`


    """

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
