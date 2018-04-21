#Calculate n. The numbered day of the year, for example January 1st is n=1.
import datetime
import pytest

def nth_day(year, month, day):
	mydate=datetime.date(year, month, day)
	return mydate.strftime('%j')

def test_answer():
	assert nth_day(2019, 02, 12) == 43

if __name__ == '__main__':
	print test_answer()
