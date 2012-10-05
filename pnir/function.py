from ifs import IFS

class Function(IFS):
    """
    A simple special case of an iterated function system (IFS) with a single
    function.  The __call__ method binds arguments to Variables in the IFS and
    retrieves the rval's final value.
    """

    def __init__(self, states, egraph, params, rval):
        IFS.__init__(self, states, routines)
        self.params = params

    def __call__(self, *args, **kwargs):
        # XXX bind args and kwargs to self.params
        raise NotImplementedError()

