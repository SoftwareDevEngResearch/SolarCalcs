#Calculate the declination angle

import Calculate_n as n
import math

#Using equation 2.23 from the 3d Edition of Principles of Solar Engineering by D. Yogi Goswami

#Find the declination angle for the specific day
def declination_angle(year, month, day):
	#Do the math inside the parentheses around sin and convert into radians
	inside_sin = math.radians((360 * (284 + int(n.nth_day(year, month, day))))/(float(365)))

	#final answer
	return 23.45* math.sin ((inside_sin) ) #returns a number with units of Degrees


