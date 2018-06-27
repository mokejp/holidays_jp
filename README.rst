******************************
holidays-jp: Japanese holidays
******************************

[![Build Status](https://travis-ci.org/mokejp/holidays_jp.svg?branch=master)](https://travis-ci.org/mokejp/holidays_jp)

holidays-jp is a library for calculate holidays.
Mainly it has been optimized to Japanese.

It can be used in standalone and does not depend on Google calendar.

Usage:

.. code-block:: python
    
    from holidays_jp import CountryHolidays
    # get japanese holidays in 2015.
    holidays = CountryHolidays.get('JP', 2015)
    # [
    #     (datetime.datetime(2015, 1, 1, 0, 0), '元日'),
    #     (datetime.datetime(2015, 1, 12, 0, 0), '成人の日'),
    #     (datetime.datetime(2015, 2, 11, 0, 0), '建国記念の日'),
    #     (datetime.datetime(2015, 3, 21, 0, 0), '春分の日'),
    #     (datetime.datetime(2015, 4, 29, 0, 0), '昭和の日'),
    #     (datetime.datetime(2015, 5, 3, 0, 0), '憲法記念日'),
    #     (datetime.datetime(2015, 5, 4, 0, 0), 'みどりの日'),
    #     (datetime.datetime(2015, 5, 5, 0, 0), 'こどもの日'),
    #     (datetime.datetime(2015, 5, 6, 0, 0), '振替休日'),
    #     (datetime.datetime(2015, 7, 20, 0, 0), '海の日'),
    #     (datetime.datetime(2015, 9, 21, 0, 0), '敬老の日'),
    #     (datetime.datetime(2015, 9, 22, 0, 0), '国民の休日'),
    #     (datetime.datetime(2015, 9, 23, 0, 0), '秋分の日'),
    #     (datetime.datetime(2015, 10, 12, 0, 0), '体育の日'),
    #     (datetime.datetime(2015, 11, 3, 0, 0), '文化の日'),
    #     (datetime.datetime(2015, 11, 23, 0, 0), '勤労感謝の日'),
    #     (datetime.datetime(2015, 12, 23, 0, 0), '天皇誕生日')
    # ]
    
    # get japanese holidays in 2015-2016.
    holidays = CountryHolidays.between('JP', 2015, 2016)
    
    # get USA holidays in 2015
    holidays = CountryHolidays.get('US', 2015)
