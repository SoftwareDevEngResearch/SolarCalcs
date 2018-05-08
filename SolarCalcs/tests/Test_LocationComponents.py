#Testing set for the LocationComponents.py file

import pytest
import LocationComponents as lp

#Basic city tests. These tests ensure that latitude and longitudate values are be obtained from just the City and State
a=lp.LocationComponents('Portland OR')
def test_basic_city():
	assert a.LonitudeValue() == pytest.approx(-122.676, rel=1e-2)
	assert a.LatitudeValue() == pytest.approx(45.523, rel=1e-2)


b = lp.LocationComponents('Portland, OR')
def test_basic_city2():
	assert b.LonitudeValue() == pytest.approx(-122.6765, rel=1e-2)
	assert b.LatitudeValue() == pytest.approx(45.5231, rel=1e-2)


#Test with full address. This tests gets lat and long from a complete address
c = lp.LocationComponents ('301 S 2nd St, Springfield, IL 62701')
def test_basic3():
	assert c.LonitudeValue() == pytest.approx(-89.6708, rel=1e-2)
	assert c.LatitudeValue() == pytest.approx(39.7639, rel=1e-2)

#Test a city name without a state. 
d = lp.LocationComponents ('Las Vegas')
def test_city_no_state():
	assert d.LonitudeValue() == pytest.approx(-115.1398, rel=1e-2)
	assert d.LatitudeValue() == pytest.approx(36.1699, rel=1e-2)

#Test an address without City and State information


#The following tests are expected to fail

#Input name without quotes
#Input misspelled city





