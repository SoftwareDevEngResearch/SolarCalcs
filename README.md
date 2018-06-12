# SolarCalcs

Overview:
 This project was to calculate the solar time of the location,
 declination angle, hour angle, altitude angle, zenith angle, and
 azimuth angle from a user given location, date, and time.

 The goal of this project is to make calculating these values quick and easy
 to make analyzing different solar technologies less time consuming.

License:
 This code is licensed with the MIT license. 

How to Use:
 Currently, the code is setup to be run in the terminal. In the terminal, move to the SolarCalcs file and run the following command:

 	python Angles.py Angles('[City, State]’ , [year], [month] , [day], [hour], [minutes], [seconds]).all_angles()
	
	--or--

	python Angles_DayLightSavings.py Angles_DayLightSavings('[City, State]’ , [year], [month] , [day], [hour], [minutes] , [seconds]).all_angles()

 Example: For Nashville, TN on August 21st, 2017 at 1:30pm during day light savings.
 python Angles_DayLightSavings.py Angles_DayLightSavings('Nashville, TN’ , 2017, 8 , 21, 12, 30 , 00).all_angles()

Variables Notes:
 Location: Works best as a “City, State” entry but can work as a full detailed address. Surround with quotations.
 Date: Year value should be 4 digits. Months should not start with zero (for May type 5 instead of 05). Day value should be 2 digits.
 Time: Uses 24hr format, requires values for hour, minutes, and seconds. Use 2 digits for each value (for 5:15pm type 17, 15, 00).

Program Output:
 This project is designed to create a unique plain text file that will be saved in the same folder as the rest of the SolarCalcs package. 
 This file will be named with the location, date, and time information as the title.
 Example: For Nashville, TN on August 21st, 2017 at 1:30pm during day light savings the file name
 will be SolarCalcs_DayLightSavings_Nashv_2017_8_21_13300.txt









