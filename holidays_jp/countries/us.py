# -*- coding: utf-8 -*-
from dateutil.rrule import rrule, YEARLY, MO, TH
from datetime import datetime, timedelta
from holidays_jp import (
    Holiday,
    Substitute,
    CountryHolidays,
    define_country_holidays,
)


def US_substitute(self, _list):
    ''' アメリカの祝日 - 振替休日 '''
    for i, holiday in enumerate(_list):
        weekday = holiday[0].isoweekday()
        if weekday == 6:
            # 土曜
            _list[i] = (holiday[0] + timedelta(days=-1), holiday[1])
        elif weekday == 7:
            # 日曜
            _list[i] = (holiday[0] + timedelta(days=1), holiday[1])

define_country_holidays(
    'US',
    CountryHolidays([
        Holiday('New Year\'s Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=1, bymonthday=1)),
        Holiday('Martin Luther King Jr.\'S Birthday',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=1, byweekday=MO, bysetpos=3)),
        Holiday('Washington\'s Birthday',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=2, byweekday=MO, bysetpos=3)),
        Holiday('Memorial Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=5, byweekday=MO, bysetpos=-1)),
        Holiday('Independence Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=7, bymonthday=4)),
        Holiday('Labor Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=9, byweekday=MO, bysetpos=1)),
        Holiday('Columbus Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=10, byweekday=MO, bysetpos=2)),
        Holiday('Veterans Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=11, bymonthday=11)),
        Holiday('Thanksgiving Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=11, byweekday=TH, bysetpos=4)),
        Holiday('Christmas Day',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=12, bymonthday=25)),
    ], [
        Substitute(None, None, None, US_substitute),
    ])
)
