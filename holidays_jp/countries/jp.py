# -*- coding: utf-8 -*-
from dateutil.rrule import rrule, YEARLY, MO, TH
from datetime import datetime, timedelta
from holidays_jp import (
    Holiday,
    Substitute,
    CountryHolidays,
    define_country_holidays,
)


def JP_vernal_equinox_day(_date):
    ''' 日本の祝日 - 春分の日 '''
    if _date.month != 3:
        return False
    year = _date.year - 1980
    if _date.year >= 2100:
        return _date.day == int(21.8510 + 0.242194 * year - int(year / 4))
    elif _date.year >= 1980:
        return _date.day == int(20.8431 + 0.242194 * year - int(year / 4))
    else:
        return _date.day == int(20.8357 + 0.242194 * year - int(year / 4))


def JP_autumnal_equinox_day(_date):
    ''' 日本の祝日 - 秋分の日 '''
    if _date.month != 9:
        return False
    year = _date.year - 1980
    if _date.year >= 2100:
        return _date.day == int(24.2488 + 0.242194 * year - int(year / 4))
    elif _date.year >= 1980:
        return _date.day == int(23.2488 + 0.242194 * year - int(year / 4))
    else:
        return _date.day == int(23.2588 + 0.242194 * year - int(year / 4))


def JP_national_holiday_1985(_date):
    ''' 日本の祝日 - 国民の休日(旧制) '''
    weekday = _date.isoweekday()
    return weekday != 1 and weekday != 7


def JP_national_holiday(self, _list):
    ''' 日本の祝日 - 国民の休日(9月) '''
    append_list = []
    fst = None
    snd = None
    for i, holiday in enumerate(_list):
        if self.dtstart is not None and self.dtstart > holiday[0]:
            continue
        if self.until is not None and self.until < holiday[0]:
            continue
        if holiday[0].month != 9:
            fst = None
            snd = None
            continue
        if not fst:
            fst = (i, holiday)
        else:
            snd = (i, holiday)
        if fst is not None and snd is not None \
           and snd[1][0].day - fst[1][0].day == 2:
            target = datetime(
                snd[1][0].year, snd[1][0].month, snd[1][0].day - 1)
            weekday = target.isoweekday()
            if weekday != 1 and weekday != 7:
                append_list.append((target, self.title))
            fst = None
            snd = None
    _list.extend(append_list)


def JP_substitute_1973(self, _list):
    ''' 日本の祝日 - 振替休日(旧制) '''
    append_list = []
    for i, holiday in enumerate(_list):
        next_holiday = None
        if i + 1 < len(_list):
            next_holiday = _list[i + 1][0]
        if self.dtstart is not None and self.dtstart > holiday[0]:
            continue
        if self.until is not None and self.until < holiday[0]:
            continue
        weekday = holiday[0].isoweekday()
        if weekday == 7 and next_holiday != holiday[0]:
            # 日曜かつ翌日が祝日でない場合翌日を振替休日とする
            append_list.append((holiday[0] + timedelta(days=1), self.title))
    _list.extend(append_list)


def JP_substitute(self, _list):
    ''' 日本の祝日 - 振替休日 '''
    append_list = []
    for i, holiday in enumerate(_list):
        if self.dtstart is not None and self.dtstart > holiday[0]:
            continue
        if self.until is not None and self.until < holiday[0]:
            continue
        weekday = holiday[0].isoweekday()
        next_day = holiday[0]
        if weekday == 7:
            # 日曜
            appended = False
            for j in range(i + 1, len(_list)):
                next_holiday = _list[j][0]
                next_day = next_day + timedelta(days=1)
                if next_holiday != next_day:
                    append_list.append((next_day, self.title))
                    appended = True
                    break
            if not appended:
                append_list.append(
                    (holiday[0] + timedelta(days=1), self.title))
    _list.extend(append_list)


define_country_holidays(
    'JP',
    CountryHolidays([
        Holiday('元日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=1, bymonthday=1)),
        Holiday('成人の日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      until=datetime(1999, 12, 31),
                      bymonth=1, bymonthday=15)),
        Holiday('成人の日',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      bymonth=1, byweekday=MO, bysetpos=2)),
        Holiday('建国記念の日',
                rrule(YEARLY,
                      dtstart=datetime(1966, 6, 25),
                      bymonth=2, bymonthday=11)),
        Holiday('春分の日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=3, bymonthday=(20, 21)),
                JP_vernal_equinox_day),
        Holiday('昭和の日',
                rrule(YEARLY,
                      dtstart=datetime(2007, 1, 1),
                      bymonth=4, bymonthday=29)),
        Holiday('みどりの日',
                rrule(YEARLY,
                      dtstart=datetime(1989, 2, 17),
                      until=datetime(2006, 12, 31),
                      bymonth=4, bymonthday=29)),
        Holiday('憲法記念日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=5, bymonthday=3)),
        Holiday('国民の休日',
                rrule(YEARLY,
                      dtstart=datetime(1985, 12, 27),
                      until=datetime(2006, 12, 31),
                      bymonth=5, bymonthday=4),
                JP_national_holiday_1985),
        Holiday('みどりの日',
                rrule(YEARLY,
                      dtstart=datetime(2007, 1, 1),
                      bymonth=5, bymonthday=4)),
        Holiday('こどもの日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=5, bymonthday=5)),
        Holiday('海の日',
                rrule(YEARLY,
                      dtstart=datetime(1996, 1, 1),
                      until=datetime(2002, 12, 31),
                      bymonth=7, bymonthday=20)),
        Holiday('海の日',
                rrule(YEARLY,
                      dtstart=datetime(2003, 1, 1),
                      until=datetime(2019, 12, 31),
                      bymonth=7, byweekday=MO, bysetpos=3)),
        Holiday('海の日',
                rrule(YEARLY,
                      dtstart=datetime(2020, 7, 23),
                      until=datetime(2020, 7, 23),
                      bymonth=7, bymonthday=23)),
        Holiday('海の日',
                rrule(YEARLY,
                      dtstart=datetime(2021, 1, 1),
                      bymonth=7, byweekday=MO, bysetpos=3)),
        Holiday('山の日',
                rrule(YEARLY,
                      dtstart=datetime(2016, 1, 1),
                      until=datetime(2019, 12, 31),
                      bymonth=8, bymonthday=11)),
        Holiday('山の日',
                rrule(YEARLY,
                      dtstart=datetime(2020, 8, 10),
                      until=datetime(2020, 8, 10),
                      bymonth=8, bymonthday=10)),
        Holiday('山の日',
                rrule(YEARLY,
                      dtstart=datetime(2021, 1, 1),
                      bymonth=8, bymonthday=11)),
        Holiday('敬老の日',
                rrule(YEARLY,
                      dtstart=datetime(1966, 6, 25),
                      until=datetime(2002, 12, 31),
                      bymonth=9, bymonthday=15)),
        Holiday('敬老の日',
                rrule(YEARLY,
                      dtstart=datetime(2003, 1, 1),
                      bymonth=9, byweekday=MO, bysetpos=3)),
        Holiday('秋分の日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=9, bymonthday=(22, 23, 24)),
                JP_autumnal_equinox_day),
        Holiday('体育の日',
                rrule(YEARLY,
                      dtstart=datetime(1966, 6, 25),
                      until=datetime(1999, 12, 31),
                      bymonth=10, bymonthday=10)),
        Holiday('体育の日',
                rrule(YEARLY,
                      dtstart=datetime(2000, 1, 1),
                      until=datetime(2019, 12, 31),
                      bymonth=10, byweekday=MO, bysetpos=2)),
        Holiday('スポーツの日',
                rrule(YEARLY,
                      dtstart=datetime(2020, 7, 24),
                      until=datetime(2020, 7, 24),
                      bymonth=7, bymonthday=24)),
        Holiday('スポーツの日',
                rrule(YEARLY,
                      dtstart=datetime(2021, 1, 1),
                      bymonth=10, byweekday=MO, bysetpos=2)),
        Holiday('文化の日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=11, bymonthday=3)),
        Holiday('勤労感謝の日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      bymonth=11, bymonthday=23)),
        Holiday('天皇誕生日',
                rrule(YEARLY,
                      dtstart=datetime(1948, 7, 20),
                      until=datetime(1989, 2, 16),
                      bymonth=4, bymonthday=29)),
        Holiday('天皇誕生日',
                rrule(YEARLY,
                      dtstart=datetime(1989, 2, 17),
                      until=datetime(2018, 12, 31),
                      bymonth=12, bymonthday=23)),
        Holiday('皇太子明仁親王の結婚の儀',
                rrule(YEARLY,
                      dtstart=datetime(1959, 4, 10),
                      until=datetime(1959, 4, 10),
                      bymonth=4, bymonthday=10)),
        Holiday('昭和天皇の大喪の礼',
                rrule(YEARLY,
                      dtstart=datetime(1989, 2, 24),
                      until=datetime(1989, 2, 24),
                      bymonth=2, bymonthday=24)),
        Holiday('即位礼正殿の儀',
                rrule(YEARLY,
                      dtstart=datetime(1990, 11, 12),
                      until=datetime(1990, 11, 12),
                      bymonth=11, bymonthday=12)),
        Holiday('皇太子徳仁親王の結婚の儀',
                rrule(YEARLY,
                      dtstart=datetime(1993, 6, 9),
                      until=datetime(1993, 6, 9),
                      bymonth=6, bymonthday=9)),
    ], [
        Substitute('国民の休日', datetime(2007, 1, 1), None, JP_national_holiday),
        Substitute('振替休日', datetime(1973, 4, 12), datetime(2006, 12, 31),
                   JP_substitute_1973),
        Substitute('振替休日', datetime(2007, 1, 1), None, JP_substitute),
    ])
)
