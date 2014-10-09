#!/usr/bin/env python

from setuptools import setup

setup(
    name='flaskblog',
    version='0.1',
    long_description=__doc__,
    packages=['flaskblog'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)