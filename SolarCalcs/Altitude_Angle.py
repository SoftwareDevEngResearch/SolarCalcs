#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: Altitude_Angle.py
# Description: Calculates the altitude angle for the given location and time
# Note: This file depends on the Solar_Time.py file.

import math
import LocationComponents as LC 
import DeclinationAngle as dels
import Hour_Angle as hrs

class Altitude_Angle():
	def __init__(self, address, year, month, day, hour, minutes, seconds):
		self.address = address
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minutes = minutes
		self.seconds = seconds
		self.latitude = LC.LocationComponents(self.address).latitude_value()
		self.ds = dels.declination_angle(self.year, self.month, self.day)
		self.hs = hrs.Hour_Angle(self.address, self.year, self. month, self.day, self.hour, self.minutes, self.seconds).hour_angle()
		self.hs_dls = hrs.Hour_Angle(self.address, self.year, self. month, self.day, self.hour, self.minutes, self.seconds).hour_angle_daylightsavings()


	def altitude(self):
		return math.asin(math.radians ((math.sin(self.latitude) * math.sin(self.ds)) + (math.cos(self.latitude) * math.cos(self.ds) * math.cos(self.hs))) )

	def altitude_daylightsavings(Self):
		return math.asin(math.radians ((math.sin(self.latitude) * math.sin(self.ds)) + (math.cos(self.latitude) * math.cos(self.ds) * math.cos(self.hs_dls))) )

if __name__ == '__main__':
	a = Altitude_Angle('Nashville, TN', 2017, 8, 21, 13, 30, 00)
	print a.altitude_daylightsavings()