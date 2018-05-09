#Calculate n. The numbered day of the year, for example January 1st is n=1.
import datetime
import pytest

def nth_day(year, month, day):
	""" Find the day of the year """

	mydate=datetime.date(year, month, day)
	return mydate.strftime('%j')


