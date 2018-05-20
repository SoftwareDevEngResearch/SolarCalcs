#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: Hour_Angle.py
# Description: Calculates the angle hour from the given time
# Note: This file depends on the Solar_Time.py file.

import Solar_Time as ST 
import datetime

#find the solar time for a given time

class Hour_Angle():

	def __init__(self, address, year, month, day, hour, minutes, seconds):
		self.address = address
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minutes = minutes
		self.seconds = seconds

	def solartime(self):
		"""Importing the solar time calculation from Solar_Time.py""" 
		return ST.Solar_Time(self.address, self.year, self. month, self.day, self.hour, self.minutes, self.seconds).solar_time()

#calculate the mintues from solar noon
	def hour_angle(self):
		"""This function calculates the minutes from solar noon and returns the hour angle"""
		#turn the solar time into total seconds (since midnight)
		seconds_solartime = self.solartime().hour*3600 + self.solartime().minute*60 + self.solartime().second

		seconds_from_solar_noon = abs(seconds_solartime - 12*3600)#noon in seconds		
		return float((seconds_from_solar_noon/60)/4) #units = degrees

	def hour_angle_daylightsavings(self):
		"""This function calculates the minutes from solar noon and returns the hour angle during DAYLIGHT SAVINGS"""

		#turn the solar time into total seconds (since midnight), subtract 1 hour for daylight saings
		seconds_solartime_2 = self.solartime().hour*3600 + self.solartime().minute*60 + self.solartime().second - 3600
		seconds_from_solar_noon_2 = abs(seconds_solartime_2 - 12*3600)#noon in seconds
		print float((seconds_from_solar_noon_2/60))
		return (float(seconds_from_solar_noon_2/60)/4) #units = degrees

if __name__ == '__main__':
	a = Hour_Angle('Nashville, TN', 2017, 8, 21, 13, 30, 00)
	print a.hour_angle_daylightsavings()

##################Numbers are correct, except for rounding



