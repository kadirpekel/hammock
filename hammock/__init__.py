import requests

class Hammock(object):
    """Chainable, magical class helps you make requests to RESTful services"""

    HTTP_METHODS = ['get', 'options', 'head', 'post', 'put', 'patch', 'delete']

    def __init__(self, name=None, parent=None, session=None):
        """Constructor

        Arguments:
            name -- name of node
            parent -- parent node for chaining
            session -- `requests` session instance
        """
        self._name = name
        self._parent = parent
        self._session = session

    def __getattr__(self, name):
        """ Here comes some magic. Any absent attribute typed within class falls
        here and return a new child `Hammock` instance in the chain.
        """
        return Hammock(name=name, parent=self)

    def __iter__(self):
        """ Iterator implementation which iterates over `Hammock` chain."""
        current = self
        while current:
            if current._name:
                yield current
            current = current._parent

    def _chain(self, *args):
        """ This method converts args into chained Hammock instances

        Arguments:
            *args -- array of string representable objects
        """
        chain = self
        for arg in args:
            chain = Hammock(name=str(arg), parent=chain)
        return chain

    def _probe_session(self):
        """This method searches for a `requests` session sticked to any
        ascending parent `Hammock` instance
        """
        for hammock in self:
            if hammock._session:
                return hammock._session
        return None

    def __call__(self, *args):
        """ Here comes second magic. If any `Hammock` instance called it returns
        a new child `Hammock` instance in the chain
        """
        return self._chain(*args)

# Bind `requests` module HTTP verbs to `Hammock` class as static methods
def bind_method(method):
    def f(hammock, *args, **kwargs):
        path_comps = [mock._name for mock in hammock._chain(*args)] 
        url = "/".join(reversed(path_comps))
        session = hammock._probe_session() or requests
        return session.request(method, url, **kwargs)
    return f

for method in Hammock.HTTP_METHODS:
    setattr(Hammock, method.upper(), bind_method(method))