Hammock!
========

Hammock is a fun module lets you deal with rest APIs by converting them into dead simple programmatic APIs.
It uses popular `requests` module in backyard to provide full-fledged rest experience.

Proof
-----

Let's play with github::

    >>> from hammock import Hammock as Github

    >>> # This generates a url such as below and requests it via http GET
    >>> resp = Github('https://api.github.com').repos('kadirpekel', 'hammock').watchers.GET()

    >>> print(resp.url)
    https://api.github.com/repos/kadirpekel/hammock/watchers

    >>> # now you're ready to take a rest for the rest the of code :)
    >>> for watcher in resp.json: print watcher.get('login')
    kadirpekel
    ...
    ..
    .

Not convinced? This is how you watch this project to see its future capabilities::

    >>> from hammock import Hammock as Github

    >>> resp = Github('https://api.github.com').user.watched('kadirpekel').PUT('hammock',
                                    auth=('<user>', '<pass>'), headers={'content-length': '0'})

    >>> print(resp)
    <Response [204]>

Install
-------

The best way to install Hammock is using pypi repositories via `easy_install` or `pip`::

    $ pip install hammock

Documentation
-------------

Hammock is a magical, polymorphic(!), fun and simple class which helps you generate RESTful urls
and lets you send requests to them using `requests` module in an easy and slick way.

Below the phrases all generates the same urls. Note that some of them are nonsense in this context::

    >>> import hammock

    >>> hammock.Hammock('http://localhost:8000').users('foo').posts('bar').comments.GET().url
    http://localhost:8000/users/foo/posts/bar/comments

    >>> hammock.Hammock('http://localhost:8000').users.foo.posts('bar').GET('comments').url
    http://localhost:8000/users/foo/posts/bar/comments

    >>> hammock.Hammock('http://localhost:8000').users.foo.posts.bar.comments.GET().url
    http://localhost:8000/users/foo/posts/bar/comments

    >>> hammock.Hammock('http://localhost:8000').users('foo', 'posts', 'comments').GET().url
    http://localhost:8000/users/foo/posts/bar/comments

    >>> hammock.Hammock('http://localhost:8000')('users')('foo', 'posts').GET('bar', 'comments').url
    http://localhost:8000/users/foo/posts/bar/comments

    >>> # Any other combinations ...

Hammock class instance provides `requests` module's all http methods binded on itself as uppercased version
while dropping the first arg 'url'. But you can continue providing any keyword argument for corresponding
http verb method of `requests` module::

    Hammock.[GET, HEAD, OPTIONS, POST, PUT, PATCH, DELETE](**kwargs)

Return type is the same `Request` object `requests` module provides.

Licence
-------
Copyright (c) 2012 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
