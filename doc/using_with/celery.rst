.. _using_with_celery:

Using with Celery
=================
`Celery <http://celeryproject.org>`_ is an asynchronous task queue/job queue
based on distributed message passing.

Usage in a Worker
-----------------
Workers in celery may be created by spawning new processes or threads from the
celeryd process.  The
`multiprocessing <http://docs.python.org/library/multiprocessing.html>`_
module is used to spawn new worker processes, while
`eventlet <http://eventlet.net/>`_ is used to spawn new worker green threads.

:mod:`multiprocessing`
----------------------
The :class:`~.ConnectionPool` class is not :mod:`multiprocessing`-safe. Because
celery evaluates globals prior to spawning new worker processes, a global
:class:`~.ConnectionPool` will be shared among multiple processes. This is
inherently unsafe and will result in race conditions.

Instead of having celery spawn multiple child processes, it is recommended that
you set
`CELERYD_CONCURRENCY <http://docs.celeryproject.org/en/latest/configuration.html#celeryd-concurrency>`_
to 1 and start multiple separate celery processes. The process argument
``--pool=solo`` may also be used when starting the celery processes.

:mod:`eventlet`
---------------
Because the :class:`~.ConnectionPool` class uses concurrency primitives from
the :mod:`threading` module, it should be possible to support
:mod:`eventlet` worker threads after 
`monkey patching <http://eventlet.net/doc/basic_usage.html#patching-functions>`_
the standard library.  However, this option has not yet been well explored.

Usage as a Broker Backend
=========================
**pycassa** is not currently a broker backend option.
