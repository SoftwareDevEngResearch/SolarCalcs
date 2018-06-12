#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: Calculate_n.py
# Description: Calculates the numbered day of the year, for example January 1st is n=1.
# Note: Date is in YY, MM, DD format

import datetime

def nth_day(year, month, day):
	""" Find the number day of the year """
	mydate=datetime.date(year, month, day)
	return mydate.strftime('%j')




