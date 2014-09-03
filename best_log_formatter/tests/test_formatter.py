from freezegun import freeze_time
import sure

from datetime import datetime
import logging
from pytz import UTC
from textwrap import dedent

from ..formatter import Formatter


class Handler(logging.Handler):

    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.record = None

    def handle(self, record):
        self.record = record


@freeze_time(datetime(2014, 8, 8, 5, 13, 59, 214672, tzinfo=UTC))
def test_log_format():

    logger = logging.Logger(name='bill.lumbergh')
    handler = Handler()
    logger.addHandler(handler)

    logger.info("Status is %s.", "nominal")

    Formatter().format(handler.record).should.equal(
        '2014-08-08T05:13:59,214+0000 bill.lumbergh INFO Status is nominal.'
    )


@freeze_time(datetime(2014, 8, 8, 5, 13, 59, 214672, tzinfo=UTC))
def test_log_format_multiline():

    logger = logging.Logger(name='tom.smykowski')
    handler = Handler()
    logger.addHandler(handler)

    logger.error(dedent("""
        Everything is screwed
        We're all gonna die
        Send help""").strip())

    Formatter().format(handler.record).should.equal(dedent("""
        2014-08-08T05:13:59,214+0000 tom.smykowski ERROR Everything is screwed
        \tWe're all gonna die
        \tSend help""").strip())
