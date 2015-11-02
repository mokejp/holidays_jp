# -*- coding: utf-8 -*-
import unittest
import datetime


class HolidayTest(unittest.TestCase):
    def assertHoliday(self, holiday, date, name):
        self.assertEqual(holiday[0], date)
        self.assertEqual(holiday[1], name)

    def testJP2015(self):
        from holidays_jp import CountryHolidays
        holidays = CountryHolidays.get('JP', 2015)
        self.assertEqual(len(holidays), 17)
        self.assertHoliday(holidays[0], datetime.datetime(2015, 1, 1), '元日')
        self.assertHoliday(holidays[1], datetime.datetime(2015, 1, 12), '成人の日')
        self.assertHoliday(holidays[2], datetime.datetime(2015, 2, 11), '建国記念の日')
        self.assertHoliday(holidays[3], datetime.datetime(2015, 3, 21), '春分の日')
        self.assertHoliday(holidays[4], datetime.datetime(2015, 4, 29), '昭和の日')
        self.assertHoliday(holidays[5], datetime.datetime(2015, 5, 3), '憲法記念日')
        self.assertHoliday(holidays[6], datetime.datetime(2015, 5, 4), 'みどりの日')
        self.assertHoliday(holidays[7], datetime.datetime(2015, 5, 5), 'こどもの日')
        self.assertHoliday(holidays[8], datetime.datetime(2015, 5, 6), '振替休日')
        self.assertHoliday(holidays[9], datetime.datetime(2015, 7, 20), '海の日')
        self.assertHoliday(holidays[10], datetime.datetime(2015, 9, 21), '敬老の日')
        self.assertHoliday(holidays[11], datetime.datetime(2015, 9, 22), '国民の休日')
        self.assertHoliday(holidays[12], datetime.datetime(2015, 9, 23), '秋分の日')
        self.assertHoliday(holidays[13], datetime.datetime(2015, 10, 12), '体育の日')
        self.assertHoliday(holidays[14], datetime.datetime(2015, 11, 3), '文化の日')
        self.assertHoliday(holidays[15], datetime.datetime(2015, 11, 23), '勤労感謝の日')
        self.assertHoliday(holidays[16], datetime.datetime(2015, 12, 23), '天皇誕生日')

    def testJPBetween(self):
        from holidays_jp import CountryHolidays
        holidays = CountryHolidays.between('JP', 1948, 2015)
        year_count = {}
        for holiday in holidays:
            if holiday[0].year not in year_count:
                year_count[holiday[0].year] = 0
            year_count[holiday[0].year] += 1
        for year in year_count:
            self.assertTrue(year_count[year] > 1)
