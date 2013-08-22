dogstatsd-python
================

A DogStatsd Python client.

[![Build Status](https://secure.travis-ci.org/DataDog/dogstatsd-python.png)](http://travis-ci.org/DataDog/dogstatsd-python)

Quick Start Guide
-----------------

First install the library with `pip` or `easy_install`

    # Install in system python ...
    sudo easy_install dogstatsd-python

    # .. or into a virtual env
    easy_install  dogstatsd-python

Then start instrumenting your code:

``` python
# Import the module.
from statsd import statsd

# Import the module.
from statsd import statsd

# Optionally, configure the host and port if you're running Statsd on a
# non-standard port.
statsd.connect('localhost', 8125)

# Increment a counter.
statsd.increment('page.views')

# Record a gauge 50% of the time.
statsd.gauge('users.online', 123, sample_rate=0.5)

# Sample a histogram.
statsd.histogram('file.upload.size', 1234)

# Time a function call.
@statsd.timed('page.render')
def render_page():
    # Render things ...

# Tag a metric.
statsd.histogram('query.time', 10, tags = ["version:1"])
```

Documentation
-------------

Read the full API docs
[here](http://dogstatsd-python.readthedocs.org/en/latest/index.html).

Feedback
--------

To suggest a feature, report a bug, or general discussion, head over
[here](http://github.com/DataDog/dogstatsd-python/issues/).

Change Log
----------

- 0.3
    - Uses a connected socket for a big performance improvemen (thanks to @Julian)
    - Use `connect` to override the host and port of a statsd instance
- 0.2.1
    - Fixed the `timed` decorator, to ensure it preserves function attributes.
- 0.2
    - Added the `set` metric type.
- 0.1
    - Initial version of the code


License
-------

Copyright (c) 2012 Datadog Inc.
