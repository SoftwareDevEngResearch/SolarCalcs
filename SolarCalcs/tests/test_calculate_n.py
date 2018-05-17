#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: test_calculate_n.py
# Description: Testing set for the Calculate_n.py file.

from .. import Calculate_n as C
import pytest

#Basic test
def test_basic():
	assert C.nth_day(2019, 01, 01) == '001'

#Test that leap years are handled correctly

	#February 29th is counted for
def test_leapyear(): 
	assert C.nth_day(2020, 03, 05) == '065'

	#Before Feb 29th, days should be counted as normal
def test_leapyear2():
	assert C.nth_day(2020, 02, 27) == '058'


#Test for a date in the past
def test_pastdate():
	assert C.nth_day(1990, 11, 29) == '333'

#Test that days greater than 31 can't be called. (Expected fail)
def test_day32():
	with pytest.raises(ValueError):
		C.nth_day(2018, 01, 32)

#Test incorrectly formated dates
def test_incorrect_format_year():
	with pytest.raises(ValueError):
		C.nth_day(18, 01, 31) #'18' instead of '2018'

def test_incorrect_format_month(): #this should pass
	assert C.nth_day(2018, 1, 31) == '031' #'1' instead of '01'

def test_incorrect_format_month2():
	with pytest.raises(ValueError):
		C.nth_day(2018, 13, 31) #month number exceeding 12

def test_incorrect_format_day():
	assert C.nth_day(2018, 01, 6) == '006' #'6' instead of '06'






