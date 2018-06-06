#!/usr/bin/env python

# Author: Nicole Guymer
# Date: June, 6 2018
# File: test_Angles.py
# Description: This file tests calculates done in the Angles.py file

from .. import Angles as AN
import pytest


a = AN.Angles('Nashville, TN', 2017, 8, 21, 13, 30, 00)

#Test declination angle
def test_declination():
	assert a.declination_angle() == pytest.approx(11.75, rel=1e-2)

#Test solar time
#def test_solartime():
#	assert a.declination_angle() == pytest.approx('13:41', rel=1e-2)

#Test hour angle
def test_hourangle():
	assert a.hour_angle() == pytest.approx(25.25, rel=1e-2)

#Test altitude angle
def test_altitude():
	assert a.altitude_angle() == pytest.approx(56.65, rel=1e-2)

#Test zenith angle
def test_zenith():
	assert a.zenith_angle() == pytest.approx(33.35, rel=1e-2)

#Test azimuth angle
def test_azimuth():
	assert a.azimuth_angle() == pytest.approx(49.44, rel=1e-2)

