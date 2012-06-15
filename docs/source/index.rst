.. dogstatsd-python documentation master file, created by
   sphinx-quickstart on Thu Jun 14 19:22:15 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dogstatsd-python
================


.. automodule:: statsd

    .. autoclass:: DogStatsd
       :members:

.. module:: statsd
.. data:: statsd

    A global :class:`~statsd.DogStatsd` instance that is easily shared
    across an application's modules. Initialize this once in your application's
    set-up code and then other modules can import and use it without further
    configuration.

    >>> from statsd import statsd
    >>> statsd.host = 'localhost'
    >>> statsd.port = 8125


Source
======

The DogStatsd source is freely available on Github. Check it out `here
<https://github.com/DataDog/dogstatsd-python>`_.

Get in Touch
============

If you'd like to suggest a feature or report a bug, please add an issue `here <https://github.com/DataDog/dogstatsd-python/issues>`_. If you want to talk about DataDog in general, reach out at `datadoghq.com <http://datadoghq.com>`_.


