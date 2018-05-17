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

a = ST.Solar_Time('Franfort, KY', 2052, 9, 19, 15, 23, 00)
def test_B_1():
	return a.B()

#----------------------------------------------------------------#
"""Tests for the ET function"""

#----------------------------------------------------------------#
"""Tests for the l_st function"""

#----------------------------------------------------------------#
"""Tests for the solar_time function"""

#----------------------------------------------------------------#
"""Tests for the solar_time_daylightsavings function"""



