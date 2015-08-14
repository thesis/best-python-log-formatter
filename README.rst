best-python-log-formatter
=========================

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/cardforcoin/best-python-log-formatter
   :target: https://gitter.im/cardforcoin/best-python-log-formatter?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

A good (the best, actually) formatter for Python logging.

https://pypi.python.org/pypi/best_log_formatter/

.. image:: https://circleci.com/gh/cardforcoin/best-python-log-formatter.png?style=badge
    :target: https://circleci.com/gh/cardforcoin/best-python-log-formatter

.. pypi - Everything below this line goes into the description for PyPI.


The API
-------

There is one class in this package: ``best_log_formatter.Formatter``


The log format
--------------

Dates are all in UTC with millisecond precision.

::

    2014-08-08T05:13:59,214+0000 name.of.logger INFO Status is nominal.

For multi-line messages, all lines after the first are indented with a tab
character.

::

    2014-08-08T05:13:59,214+0000 name.of.logger ERROR This is a
        multi-line
        message.
