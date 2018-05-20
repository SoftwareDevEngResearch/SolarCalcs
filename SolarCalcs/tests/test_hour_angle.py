#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: test_hour_angle.py
# Description: Tests the Hour_Angle.py file

from .. import Hour_Angle as hs
import pytest

#test hour angle
a = hs.Hour_Angle('Nashville, TN', 2017, 8, 21, 13, 30, 00)
def test1_hs():
	#For this test, I'm assuming daylight saving doesn't exist
	assert a.hour_angle() == pytest.approx(25.25, rel = 1e-1)

#test hour angle with daylight savings
def test2_hs_daylightsavings():
	#For this test, I'm assuming daylight saving doesn't exist
	assert a.hour_angle_daylightsavings() == pytest.approx(10.25, rel = 1e-1)