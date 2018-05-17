#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: test_solar_time.py
# Description: Testing set for the Solar_Time.py file
# Note: Time is in the 24hr format

"""This file tests each of the functions inside the Solar_Time class and the class itself."""

from .. import Solar_Time as ST
import pytest


#----------------------------------------------------------------#
"""Tests for the B function"""

a = ST.Solar_Time('Nashville, TN', 2017, 8, 21, 13, 30, 00)
def test_B_1():
	assert a.B() == pytest.approx(150.33, rel=1e-2)

#----------------------------------------------------------------#
"""Tests for the ET function"""
def test_ET_1():
	assert a.ET() == pytest.approx(-2.69*60, rel=1.e-2)


#----------------------------------------------------------------#
"""Tests for the l_st function"""
def test_l_st_1():
	assert a.l_st() == int(90)

#----------------------------------------------------------------#
"""Tests for the solar_time function"""
#def test_solar_time_1():
#	assert a.soalr_time() == pytest.approx('2017-08-21 13:40:12.749108' )

#----------------------------------------------------------------#
"""Tests for the solar_time_daylightsavings function"""



