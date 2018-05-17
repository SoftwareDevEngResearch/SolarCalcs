#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: LocationComponents.py
# Description: This file uses geopy to find the latitude and longitutde values, and time zones in decimal form for user given locations.
# Note: Not all addresses or locations can be found using geopy.


from geopy.geocoders import Nominatim
from geopy import geocoders
import datetime, pytz

class LocationComponents():

	def __init__(self, address):
		self.address = address	

	def latitude_value(self):
		""" Calculate the latitude of the location """

		#Check if there is more than 1 result for the given location
		locations = Nominatim().geocode(self.address, False)

		if len(locations) > 1:
			print 'Please enter a more specific location. ie: City and State'

		else:
			return Nominatim().geocode(self.address).latitude


	def longitude_value(self):
		""" Calculate the longitude of the location """

		#Check if there is more than 1 result for the given location
		locations = Nominatim().geocode(self.address, False)
	

		if len(locations) > 1:
			print 'Please enter a more specific location. ie: City and State'
		else:
			return Nominatim().geocode(self.address).longitude

	def time_zone(self):
		"""Formating timezone for given location"""

		g = geocoders.GoogleV3()

		#Gives the name of the timezone, ex: Africa/Luanda
		timezone_name = str(g.timezone((self.latitude_value(), self.longitude_value())))

		#Returns the numeric value of the timezone, ex: +0100
		return int(pytz.timezone(timezone_name).localize(datetime.datetime(2011,1,1)).strftime('%z'))/100
