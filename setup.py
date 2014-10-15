#!/usr/bin/env python

from setuptools import setup
import app


try:
    long_description = open('README.md').read()
except:
    long_description = app.__description__


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='flaskblog',
    version=app.__version__,
    url='https://github.com/defshine/flaskblog',
    author=app.__author__,
    author_email=app.__email__,
    description=app.__description__,
    long_description=long_description,
    license=app.__license__,
    packages=['flaskblog'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIREMENTS
)