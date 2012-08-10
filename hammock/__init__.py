from wrest import Client

class Hammock(object):

    _client = None

    def __init__(self, name=None, parent=None, client_ops=dict()):
        self._name = name
        self._parent = parent

        if not self._parent and not Hammock._client:
            Hammock._client = Client(name, **client_ops)

            def bind_method(method):
                def f(self, name=None, **kwargs):
                    current = self
                    if name:
                        current = Hammock(name=name, parent=current)
                    args = [mock._name for mock in current]
                    args.reverse()
                    kwargs['method'] = method
                    return Hammock._client.rest(*args, **kwargs)
                return f

            for method in Client.HTTP_METHODS:
                setattr(Hammock, method, bind_method(method))

    def __getattr__(self, name):
        return Hammock(name=name, parent=self)

    def __iter__(self):
        current = self
        while current:
            if current._name and current._parent:
                yield current
            current = current._parent

    def __call__(self, *args):
        chain = self
        for arg in args:
            chain = Hammock(name=arg, parent=chain)
        return chain
