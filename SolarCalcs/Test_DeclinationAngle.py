#Test the DeclinationAngle.py file

import DeclinationAngle as ds
import pytest

def test_basic():
	assert ds.declination_angle(2017, 8, 21) == pytest.approx(11.75412, rel=1e-3)