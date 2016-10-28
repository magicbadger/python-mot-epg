#!/usr/bin/env python

from distutils.core import setup

setup(name='python-mot-epg',
      version='1.0.0',
      description='Plugin to the python-mot library to handle DAB EPG binary encoding as per ETSI TS 102 371', 
      author='Ben Poor',
      author_email='ben.poor@thisisglobal.com',
      packages=['mot.epg'],
      package_dir = {'' : 'src'}
     )
