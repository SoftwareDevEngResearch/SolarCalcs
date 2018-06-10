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
def test_leapyear(): 
	"""February 29th is counted for"""
	assert C.nth_day(2020, 03, 05) == '065'

def test_leapyear2():
	"""Before Feb 29th, days should be counted as normal"""
	assert C.nth_day(2020, 02, 27) == '058'

#Test for a date in the past
def test_pastdate():
	"""Should be able to calculate n for any date in the past, present, or future"""
	assert C.nth_day(1990, 11, 29) == '333'

#Expected Fail
def test_day32():
	"""Test that days greater than 31 can't be called."""
	with pytest.raises(ValueError):
		C.nth_day(2018, 01, 32)

def test_day-1():
	"""Test that days less than zero can't be called."""
	with pytest.raises(ValueError):
		C.nth_Day(2020,04, -1)

def test_day0():
	"""Test that can't call the zeroth day"""
	with pytest.raises(ValueError):
		C.nth_day(1999, 11, 0)

#Test differently formated dates
def test_incorrect_format_year():
	"""Test 2 digit year values instead of 4"""
	with pytest.raises(ValueError):
		C.nth_day(18, 01, 31) #'18' instead of '2018'

def test_format_month1(): 
	"""Test 1 digit month value"""
	assert C.nth_day(2018, 1, 31) == '031' #'1' instead of '01'

def test_incorrect_format_month1():
	"""Test 2 digit month value, should raise an error for months starting with 0."""
	with pytest.raises(ValueError):
		C.nth_day(2045, 08, 04) 

def test_incorrect_format_month2():
	with pytest.raises(ValueError):
		C.nth_day(2018, 13, 31) #month number exceeding 12

def test_format_day():
	"""Test 1 digit day ormat"""
	assert C.nth_day(2018, 01, 6) == '006'






