#Calculate the declination, zenith angle, hour angle, azimuth angle, altitude angle, and solar time

#Import the necessary part of Geopy
from geopy.geocoders import Nominatim



#Start class
class LocationComponents():

	#define inputs in terms of self
	def __init__(self, address):
		self.address = address	

	#Calculate the latitude of the location
	def LatitudeValue(self):
		return Nominatim().geocode(self.address).latitude


	#Calculate the longitude of the location
	def LonitudeValue(self):
		return Nominatim().geocode(self.address).longitude

#End class




