#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: test_locationcomponents.py
# Description: Testing set for the LocationComponents.py file

import pytest
from .. import LocationComponents as lp

#Basic city tests. These tests ensure that latitude and longitudate values are be obtained from just the City and State
a=lp.LocationComponents('Portland OR')
def test_basic_city():
	assert a.longitude_value() == pytest.approx(-122.676, rel=1e-2)
	assert a.latitude_value() == pytest.approx(45.523, rel=1e-2)


b = lp.LocationComponents('Portland, OR')
def test_basic_city2():
	assert b.longitude_value() == pytest.approx(-122.6765, rel=1e-2)
	assert b.latitude_value() == pytest.approx(45.5231, rel=1e-2)






