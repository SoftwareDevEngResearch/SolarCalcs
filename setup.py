#!/usr/bin/env python

# Author: Nicole Guymer
# Date: May, 16 2018
# File: setup.py
# Description: This file contains setup information to down the project through pip.


try:  
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='SolarCalcs',
    version='0.1.0',
    description='Calculates  the declination, zenith angle, hour angle, azimuth angle, altitude angle, and solat time for a given location, time, and date.',
    author='Nicole Guymer',
    author_email='nicole@roboticmayhem.com',
    url='',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
    ],
    license='MIT',
    python_requires='>=2',
    zip_safe=False,
    packages=['SolarCalcs', 'SolarCalcs.tests'],

    package_dir={
        'SolarCalcs': 'SolarCalcs',
        'SolarCalcs.tests': 'SolarCalcs/tests',
        },
    include_package_data=True,

)