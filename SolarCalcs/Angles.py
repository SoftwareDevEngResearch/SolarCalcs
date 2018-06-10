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


class Angles():
	def __init__(self, address, year, month, day, hour, minutes, seconds):
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
		inside_sin = math.radians((360 * (284 + int(self.n)))/(float(365)))
		#return float(23.45 * math.sin (( inside_sin) )) #returns a number with units of Degrees
		return float(23.45 * math.sin (( inside_sin) )) #returns a number with units of Degrees

	def solar_time(self):
		B = (360*( int(n.nth_day(self.year, self.month, self.day))-81) )/float(364)  #unit = degrees
		ET = ( (float(9.87)*math.sin(2*math.radians(float(B)))) - (float(7.53)*math.cos(math.radians(float(B)))) - (float(1.5)*math.sin(math.radians(float(B)))))*60 #units = seconds
		l_st = abs(LC.LocationComponents(self.address).time_zone()*15) #units = degrees
		LST = datetime.datetime(self.year, self.month, self.day, self.hour, self.minutes, self.seconds)
		long_offset = (l_st- abs(self.longitude))*4*60 #units = seconds
		return LST + datetime.timedelta(seconds = ET) + datetime.timedelta(seconds = long_offset)

	def hour_angle(self):
		"""This function calculates the minutes from solar noon and returns the hour angle"""
		#turn the solar time into total seconds (since midnight)
		seconds_solartime = self.solar_time().hour*3600 + self.solar_time().minute*60 + self.solar_time().second
		seconds_from_solar_noon = abs(seconds_solartime - 12*3600)#noon in seconds		
		return (float(seconds_from_solar_noon)/60)/4 #units = degrees

	def altitude_angle(self):
		a = math.sin(math.radians(self.latitude)) * math.sin(math.radians(self.declination_angle()))
		b = math.cos(math.radians(self.latitude)) * math.cos(math.radians(self.declination_angle())) * math.cos(math.radians(self.hour_angle()))
		c = a+b
		d = math.asin(c)
		return math.degrees(d) #units = degress

	def zenith_angle(self):
		return 90 - self.altitude_angle()

	def azimuth_angle(self):
		div = math.cos(math.radians(self.declination_angle())) * (math.sin(math.radians(self.hour_angle())) / math.cos(math.radians(self.altitude_angle())))
		return math.degrees(math.asin(div))

	def all_angles(self):
		#Create a file that holds all the values
		filename = 'SolarCalcs_%(address)s_%(year)d_%(month)d_%(day)d_%(hour)d%(minutes)d%(seconds)d.txt' % {'address': self.address[:5], 'year': self.year, 'month' :self.month, 'day': self.day, 'hour':self.hour, 'minutes': self.minutes, 'seconds':self.seconds}
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
	a = Angles('Nashville, TN', 2017, 8, 21, 13, 30, 00)
	print a.all_angles()

	#print a.declination_angle()
	#print a.solar_time()
	#print a.hour_angle()
	#print a.altitude_angle()
	#print a.zenith_angle()
	#print a.azimuth_angle()



