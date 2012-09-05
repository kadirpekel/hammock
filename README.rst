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
and lets you request them using `requests` module in an easy and slick way.

Below the all phrases make request to the same url of 'http://localhost:8000/users/foo/posts/bar/comments'.
Note that all of them are valid but some of them are nonsense in their belonging context::

    >>> import hammock
    >>> api = hammock.Hammock('http://localhost:8000')
    >>> api.users('foo').posts('bar').comments.GET()
    <Response [200]>
    >>> api.users.foo.posts('bar').GET('comments')
    <Response [200]>
    >>> api.users.foo.posts.bar.comments.GET()
    <Response [200]>
    >>> api.users('foo', 'posts', 'comments').GET()
    <Response [200]>
    >>> api('users')('foo', 'posts').GET('bar', 'comments')
    <Response [200]>
    >>> # Any other combinations ...

Hammock class instance provides `requests` module's all http methods binded on itself as uppercased version
while dropping the first arg 'url' in replacement of `*args` to let you to continue appending url components.

Also you can continue providing any keyword argument for corresponding http verb method of `requests` module::

    Hammock.[GET, HEAD, OPTIONS, POST, PUT, PATCH, DELETE](*args, **kwargs)

Return type is the same `Response` object `requests` module provides.

Here is some more real world applicable example which uses twitter api::

    >>> import hammock
    >>> twitter = hammock.Hammock('https://api.twitter.com/1')
    >>> tweets = twitter.statuses('user_timeline.json').GET(params={'screen_name':'kadirpekel', 'count':'10'}).json
    >>> for tweet in tweets: print tweet.get('text')
    my tweets
    ...
    ..
    .

You might also want to use sessions. Let's take a look at the JIRA example below which maintains basic
auth credentials through several http requests::

    >>> import hammock

    >>> # You can configure a session by providing keyword args to `Hammock` constructor to initiate builtin `requests` session
    >>> # This sample below shows the use of auth credentials through several requests by intitiating a embedded session
    >>> jira = hammock.Hammock('https://jira.atlassian.com/rest/api/latest', auth=('<user>', '<pass>'))

    >>> my_issue = 'JRA-9'

    >>> # Let's get a jira issue. No auth credentials provided explicitly since parent
    >>> # hammock already has a `requests` session configured.
    >>> issue = jira.issue(my_issue).GET()

    >>> # Now watch the issue again using with the same session
    >>> watched = jira.issue(my_issue).watchers.POST(params={'name': '<user>'})

    >>> print(watched)

More detailed, concrete documentation coming soon...

Contributors
------------

* @maraujop (Miguel Araujo)
* @rubik (Michele Lacchia)

Licence
-------
Copyright (c) 2012 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
