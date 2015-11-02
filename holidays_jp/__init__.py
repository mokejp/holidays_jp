# -*- coding: utf-8 -*-
from datetime import datetime

HOLIDAY_TABLE = {}


def define_country_holidays(country_code, holidays):
    if len(country_code) != 2:
        raise ValueError('country_code')
    if not isinstance(holidays, CountryHolidays):
        raise ValueError('holidays')
    HOLIDAY_TABLE[country_code.upper()] = holidays


class Holiday:
    ''' 祝祭日 '''
    def __init__(self, title, rrule, _filter=None):
        self.title = title
        self.rrule = rrule
        self.filter = _filter

    def between(self, _from, _to):
        dates = self.rrule.between(_from, _to, inc=True)
        dates = filter(self.filter, dates)
        return map(lambda item: (item, self.title), dates)


class Substitute:
    ''' 振替休日, その他前後の祝日が影響する祝祭日 '''
    def __init__(self, title, dtstart, until, func):
        self.title = title
        self.dtstart = dtstart
        self.until = until
        self.func = func

    def apply(self, _list):
        self.func(self, _list)


class CountryHolidays:
    ''' 国の祝祭日 '''
    def __init__(self, holidays, substitutes=None):
        self.holidays = holidays
        self.substitutes = substitutes

    def _get(self, year):
        return self.between(year, year)

    def _between(self, from_year, to_year):
        dates = []
        for holiday in self.holidays:
            dates.extend(holiday.between(
                datetime(from_year, 1, 1), datetime(to_year, 12, 31)))
        dates.sort(key=lambda item: item[0])
        if self.substitutes is not None:
            for substitute in self.substitutes:
                substitute.apply(dates)
        dates.sort(key=lambda item: item[0])
        return dates

    @classmethod
    def get(cls, country_code, year):
        return cls.between(country_code, year, year)

    @classmethod
    def between(cls, country_code, from_year, to_year):
        holiday_def = HOLIDAY_TABLE.get(country_code)
        if holiday_def is None:
            return None
        return holiday_def._between(from_year, to_year)


# load countries
from holidays_jp.countries import *
