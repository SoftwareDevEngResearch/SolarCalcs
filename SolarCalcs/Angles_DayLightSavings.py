#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 24 2018
# File: Angles.py
# Description: This file calculates the declination angle, solar time, hour angle, altitude angle,
#				zenith angle and zaimuth angle for the user given location, date, and time.
# Note: This file depends on the Calculate_n.py and LocationComponents.py files.



import math
import LocationComponents as LC
import Calculate_n as n
import datetime


class Angles_DayLightSavings():

	def __init__(self, address, year, month, day, hour, minutes, seconds):
	"""Define all the variables in terms of the class.
	Bring in the nth_day value from Calculate_n.py.
	Bring in the location values from LocationComponents.py."""
		self.address = address
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minutes = minutes
		self.seconds = seconds
		self.latitude = float(LC.LocationComponents(self.address).latitude_value())
		self.longitude = float(LC.LocationComponents(self.address).longitude_value())
		self.n = float(n.nth_day(self.year, self.month, self.day))
		self.time = datetime.time(self.hour , self.minutes, self.seconds)

	def declination_angle(self):
		"""Calculate the declination angle for the given day of the year"""
		inside_sin = math.radians((360 * (284 + int(self.n)))/(float(365)))
		return 23.45 * math.sin (( inside_sin) ) #returns a number with units of Degrees

	def solar_time(self):
		"""Calculate the solar time of the given location on the given time and day of the year. 
		The local standard time (the time shown on your clock at that location) does not match the actual solar time
		directly due to the generalization of the time zones.
		The solar time is the true time for a given location."""
		B = (360*( int(n.nth_day(self.year, self.month, self.day))-81) )/float(364)  #unit = degrees
		ET = ( (float(9.87)*math.sin(2*math.radians(float(B)))) - (float(7.53)*math.cos(math.radians(float(B)))) - (float(1.5)*math.sin(math.radians(float(B)))))*60 #units = seconds
		l_st = abs(LC.LocationComponents(self.address).time_zone()*15) #units = degrees
		LST = datetime.datetime(self.year, self.month, self.day, self.hour, self.minutes, self.seconds)
		long_offset = (l_st- abs(self.longitude))*4*60 #units = seconds
		return LST + datetime.timedelta(seconds = ET) + datetime.timedelta(seconds = long_offset) - datetime.timedelta(seconds = 3600) 

	def hour_angle(self):
		"""This function calculates the difference between the local time and solar noon, then returns the hour angle.
		This file accounts for day light savings time."""
		
		#turn the solar time into total seconds (since midnight)
		seconds_solartime = self.solar_time().hour*3600 + self.solar_time().minute*60 + self.solar_time().second
		seconds_from_solar_noon = abs(seconds_solartime - 12*3600)#noon in seconds		
		return (float(seconds_from_solar_noon)/60)/4 #units = degrees

	def altitude_angle(self):
		"""Calculate the altitude angle for the given location"""
		a = math.sin(math.radians(self.latitude)) * math.sin(math.radians(self.declination_angle()))
		b = math.cos(math.radians(self.latitude)) * math.cos(math.radians(self.declination_angle())) * math.cos(math.radians(self.hour_angle()))
		c = a+b
		d = math.asin(c)
		return math.degrees(d) #units = degress

	def zenith_angle(self):
		"""Calulate the zenith angle for the given location"""
		return 90 - self.altitude_angle()

	def azimuth_angle(self):
		"""Calculate the azimuth angle for the given time, date, and locaton"""
		div = math.cos(math.radians(self.declination_angle())) * (math.sin(math.radians(self.hour_angle())) / math.cos(math.radians(self.altitude_angle())))
		return math.degrees(math.asin(div))

	def all_angles(self):
		"""Create a text file that holds all the values from the above functions.
		This file will have a unique name containing the time, date, and location used for the calculations."""

		filename = 'SolarCalcs_DayLightSavings_%(address)s_%(year)d_%(month)d_%(day)d_%(hour)d%(minutes)d%(seconds)d.txt' % {'address': self.address[:5], 'year': self.year, 'month' :self.month, 'day': self.day, 'hour':self.hour, 'minutes': self.minutes, 'seconds':self.seconds}
		st = str(self.solar_time())
		with open('%s' % filename , 'w') as f:
			f.write('Nth Day of the Year = %f' % self.n)
			f.write('\nLatitude = %f degrees' % self.latitude)
			f.write('\nLongitude = %f degrees' %self.longitude)
			f.write('\nSolar Time = %s' % st)
			f.write('\nDeclination Angle = %f degrees' % self.declination_angle())
			f.write('\nHour Angle = %f degrees' % self.hour_angle())
			f.write('\nAltitude Angle = %f degrees' % self.altitude_angle())
			f.write('\nZenith Angle = %f degrees' % self.zenith_angle())
			f.write('\nAzimuth Angle = %f degrees\n' % self.azimuth_angle())

if __name__ == '__main__':
	a = Angles_DayLightSavings('Nashville, TN', 2017, 8, 21, 13, 30, 00)
	print a.all_angles()


