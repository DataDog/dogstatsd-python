"""

"""

import logging
from random import random
from socket import socket, AF_INET, SOCK_DGRAM
from time import time


logger = logging.getLogger('dogstatsd')


class DogStatsd(object):

    def __init__(self, host='localhost', port=8125):
        self.host = host
        self.port = port
        self.socket = socket(AF_INET, SOCK_DGRAM)

    def gauge(self, metric, value, tags=None, sample_rate=1):
        return self._send(metric, 'g', value, tags, sample_rate)

    def increment(self, metric, value=1, tags=None, sample_rate=1):
        self._send(metric, 'c', value, tags, sample_rate)

    def decrement(self, metric, value=1, tags=None, sample_rate=1):
        self._send(metric, 'c', -value, tags, sample_rate)

    def histogram(self, metric, value, tags=None, sample_rate=1):
        self._send(metric, 'h', value, tags, sample_rate)

    def timing(self, metric, value, tags=None, sample_rate=1):
        self._send(metric, 'ms', value, tags, sample_rate)

    def timed(self, metric, tags=None, sample_rate=1):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                start = time()
                result = func(*args, **kwargs)
                self.timing(metric, time() - start, tags=tags, sample_rate=sample_rate)
                return result
            return wrapped
        return wrapper

        pass

    def _send(self, metric, metric_type, value, tags, sample_rate):
        try:
            if sample_rate == 1 or random() < sample_rate:
                payload = metric + ':' + str(value) + '|' + metric_type
                if sample_rate != 1:
                    payload += '|@' + str(sample_rate)
                if tags:
                    payload += '|#' + ','.join(tags)
                # FIXME: we could make this faster by having a self.address
                # tuple that is updated every time we set the host or port.
                # Also could inline sendto.
                self.socket.sendto(payload, (self.host, self.port))
        except:
            logger.exception("Error submitting metric")

statsd = DogStatsd()
