dogstatsd-python
================

A DogStatsd Python client

[![Build Status](https://secure.travis-ci.org/DataDog/dogstatsd-python.png)](http://travis-ci.org/DataDog/dogstatsd-python)

Quick Start Guide
-----------------

First install the library with `pip` or `easy_install`

    # Install in system python ...
    sudo easy_install dogstatsd-python
    
    # .. or into a virtual env
    easy_install  dogstatsd_python

Then start instrumenting your code:


    # Load and configure the module.

    from statsd import statsd
    statsd.host = 'localhost'
    statsd.port = 8125

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

Documentation
-------------

Full API documentation is available
[here](http://www.pythondoc.info/github/DataDog/dogstatsd-ruby/master/frames).


Feedback
--------

To suggest a feature, report a bug, or general discussion, head over
[here](http://github.com/DataDog/dogstatsd-python/issues/).


License
-------

Copyright (c) 2012 Datadog Inc.
