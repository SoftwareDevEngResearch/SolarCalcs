#Test the DeclinationAngle.py file

import DeclinationAngle as ds
import pytest


#This test is a basic test to make sure the function outputs the expected number
def test_basic():
	assert ds.declination_angle(2017, 8, 21) == pytest.approx(11.75412, rel=1e-3)

#Add more tests