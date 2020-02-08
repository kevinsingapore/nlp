#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import re

strings = ['war of 1812','there are 5280 feet to a mile','happy new year 2016']

year_strings = []

for string in strings:
  if re.search('[1-2][0-9]{3}',string) is not None:
    year_strings.append(string)

print(year_strings)
