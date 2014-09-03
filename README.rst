best-python-log-formatter
=========================

A good (the best, actually) formatter for Python logging.

https://pypi.python.org/pypi/best_log_formatter/

.. pypi - Everything below this line goes into the description for PyPI.


The API
-------

There is one class in this package: ``best_log_formatter.Formatter``


The log format
--------------

Dates are all in UTC.

For multi-line messages, all lines after the first are indented with a tab
character.

.. code::

    2014-08-08T05:13:59,214+0000 name.of.logger INFO Status is nominal.

.. code::

    2014-08-08T05:13:59,214+0000 name.of.logger ERROR This is a
        multi-line
        message.
