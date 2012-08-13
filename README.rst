Hammock!
========

Hammock lets you deal with rest APIs by converting them into dead simple programmatic APIs.

How?
----
Let's play with github::

    >>> from hammock import Hammock as Github

    >>> resp = Github('https://api.github.com').repos('kadirpekel', 'hammock').watchers.GET()

    >>> # This generates a url such as below and requests it via http GET
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

Docs
----

soon.

Licence
-------
Copyright (c) 2012 Kadir Pekel.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
