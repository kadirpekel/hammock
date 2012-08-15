import requests


class Hammock(object):
    """Chainable, magical class helps you make requests to RESTful services"""

    HTTP_METHODS = ['get', 'options', 'head', 'post', 'put', 'patch', 'delete']

    def __init__(self, name=None, parent=None, **kwargs):
        """Constructor

        Arguments:
            name -- name of node
            parent -- parent node for chaining
            **kwargs -- `requests` session be initiated with if any available
        """
        self._name = name
        self._parent = parent
        self._session = kwargs and requests.session(**kwargs) or None

    def __getattr__(self, name):
        """Here comes some magic. Any absent attribute typed within class
        falls here and return a new child `Hammock` instance in the chain.
        """
        return Hammock(name=name, parent=self)

    def __iter__(self):
        """Iterator implementation which iterates over `Hammock` chain."""
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

    def _close_session(self, probe=False):
        """Closes session if exists

        Arguments:
            probe -- search through ascendants if any session available
                to close
        """
        session = probe and self._probe_session() or self._session
        if session:
            session.close()

    def __call__(self, *args):
        """Here comes second magic. If any `Hammock` instance called it
        returns a new child `Hammock` instance in the chain
        """
        return self._chain(*args)

    def _url(self, *args):
        """Converts current `Hammock` chain into a url string

        Arguments:
            *args -- extra url path components to tail
        """
        path_comps = [mock._name for mock in self._chain(*args)]
        return "/".join(reversed(path_comps))

    def __repr__(self):
        """ String representaion of current `Hammock` chain"""
        return self._url()


def bind_method(method):
    """Bind `requests` module HTTP verbs to `Hammock` class as
    static methods."""
    def aux(hammock, *args, **kwargs):
        session = hammock._probe_session() or requests
        return session.request(method, hammock._url(*args), **kwargs)
    return aux

for method in Hammock.HTTP_METHODS:
    setattr(Hammock, method.upper(), bind_method(method))
