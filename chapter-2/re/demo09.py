#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import re

year_strings = '2016 was a good year, but 2017 will be better'

years = re.findall('[2][0-9]{3}',year_strings)

print(years)
