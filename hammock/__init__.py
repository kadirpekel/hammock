from wrest import Client

class Hammock(object):

    def __init__(self, name=None, parent=None, client_ops=dict()):
        """Constructor

        Arguments:
            name -- name of node. If this node is root, used as client base_url
            parent -- parent node for chaining
            client_ops -- `wrest` client constructor options
        """
        self._name = name
        self._parent = parent

        if not self._parent:
            client = Client(client_ops.get('base_url', name), **client_ops)

            def bind_method(method):
                def f(self2, *args, **kwargs):
                    args = [mock._name for mock in self2._chain(*args)]
                    args.reverse()
                    kwargs['method'] = method
                    return client.rest(*args, **kwargs)
                return f

            for method in Client.HTTP_METHODS:
                setattr(Hammock, method, bind_method(method))

    def __getattr__(self, name):
        """ Here comes some magic. Any absent attribute typed within class falls
        here and return a new child `Hammock` instance in the chain.
        """
        return Hammock(name=name, parent=self)

    def __iter__(self):
        """ Iterator implementation which iterates over `Hammock` chain."""
        current = self
        while current:
            if current._name and current._parent:
                yield current
            current = current._parent

    def _chain(self, *args):
        """ This method converts args into chained Hammock instances

        Arguments:
            args -- array of string representable objects
        """
        chain = self
        for arg in args:
            chain = Hammock(name=str(arg), parent=chain)
        return chain

    def __call__(self, *args):
        """ Here comes second magic. If any `Hammock` instance called it returns
        a new child `Hammock` instance in the chain
        """
        return self._chain(*args)
