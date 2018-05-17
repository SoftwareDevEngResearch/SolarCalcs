#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: Solar_Time.py
# Description: Calculates the  solar time of a given location and the standard time at that location.
# Note: This file presents time in the 24hr format.

import math
import datetime
import time
import Calculate_n as n
import LocationComponents as LC


class Solar_Time():
	"""This class calculates the solar time of the location and time given by the user.
		Contained in this class are the calculations for LST, ET, and standard longitude (l_st).
		These calculations pull data from Calculate_n.py and LocationComponents.py"""

	def __init__(self, address, year, month, day, hour, minutes, seconds):
		self.address = address
		self.day = int(day)
		self.month = int(month)
		self.year = int(year)


		#Uses 24 hour time model
		self.hour = int(hour)
		self.minutes = int(minutes)
		self.seconds = int(seconds)
		time = datetime.time(self.hour , self.minutes, self.seconds)
		self.longitude = LC.LocationComponents(self.address).longitude_value()

	def B(self):
		"""Calcluate B using data from Calculat_n.py
		B is a variable used in ET."""

		return (360*( int(n.nth_day(self.year, self.month, self.day))-81) )/float(364)  #unit = degrees

	def ET(self):
		"""ET is the equation of time. This accounts for the irregularity of the earth's motion around the sun. 
		--Source: Principles of Solar Engineering, 3rd. Edition, by D. Yogi Goswami"""

		return (float(9.87)*math.sin(math.radians(2*float(self.B()))) - float(7.53)*math.cos(math.radians(float(self.B()))) - float(1.5)*math.sin(math.radians(float(self.B()))))*60 #units = seconds

	def l_st(self):
		"""Pulls the timezone information from LocationComponents.py then converts from the numeric timezone value
		to the standard longtiude associated with that timezone."""

		return abs(LC.LocationComponents(self.address).time_zone()*15) #units = degrees


#This function is not returned the expected values. It likely has to do with the how time is delt with.

	def solar_time(self):
		"""Using the above functions, calculate the solar time for the given location"""

		#Local Standard Time
		LST = datetime.datetime(self.year, self.month, self.day, self.hour, self.minutes, self.seconds)
		long_offset = (self.l_st() - abs(self.longitude))*4*60 #units = seconds
		return LST + datetime.timedelta(seconds = self.ET()) + datetime.timedelta(seconds = long_offset)

#Function to account for day light savings, if applicable to location
	def solar_time_daylightsavings(self):
		"""This function is the same as solar_time() expect that it accounts for daylight savings by subtracting an hour from the total time"""

		#Local Standard Time
		LST = datetime.datetime(self.year, self.month, self.day, self.hour, self.minutes, self.seconds)
		long_offset = (self.l_st() - abs(self.longitude))*4*60 #units = seconds

		#subtract 1 hour for daylight saving
		return LST + datetime.timedelta(seconds = self.ET()) + datetime.timedelta(seconds = long_offset) - datetime.timedelta(seconds = 3600) 



	
		






