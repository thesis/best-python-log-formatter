from __future__ import absolute_import

import logging
import re
import time


class Formatter(logging.Formatter):

    def __init__(self):
        super(Formatter, self).__init__(
            fmt='%(asctime)s %(name)s %(levelname)s %(message)s')

    def formatTime(self, record, *args, **kwargs):
        t = time.gmtime(record.created)
        return '{},{}+0000'.format(
            time.strftime('%Y-%m-%dT%H:%M:%S', t),
            int(record.msecs),
        )

    def format(self, record):
        s = super(Formatter, self).format(record)

        # Indent all lines after the first one so we can correctly
        # group lines of multiline messages.
        s = re.sub(r'(?<=\n)', '\t', s, flags=re.DOTALL)

        return s
