#Testing set for the LocationComponents.py file

import pytest
import LocationComponents as lp

#Basic city test
a=lp.LocationComponents('Portland OR')

def test_basic_city():
	assert a.LonitudeValue() == pytest.approx(-122.676, rel=1e-2)
	assert a.LatitudeValue() == pytest.approx(45.523, rel=1e-2)

#Basic city test #2, with comma in name
b = lp.LocationComponents('Portland, OR')

def test_basic_city2():
	assert b.LonitudeValue() == pytest.approx(-122.6765, rel=1e-2)
	assert b.LatitudeValue() == pytest.approx(45.5231, rel=1e-2)

#Test with full address
c = lp.LocationComponents ('301 S 2nd St, Springfield, IL 62701')
def test_basic3():
	assert c.LonitudeValue() == pytest.approx(-89.6708, rel=1e-2)
	assert c.LatitudeValue() == pytest.approx(39.7639, rel=1e-2)




