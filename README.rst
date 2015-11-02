******************************
holidays-jp: Japanese holidays
******************************

holidays-jp is a library for calculate the Japanese holidays since 1948.
It can be used in standalone and does not depend on Google calendar.

Usage:

.. code-block:: python
    
    from holidays_jp import CountryHolidays
    # get holidays in 2015.
    holidays = CountryHolidays.get('JP', 2015)
    
    # get holidays in 2015-2016.
    holidays = CountryHolidays.between('JP', 2015, 2016)
