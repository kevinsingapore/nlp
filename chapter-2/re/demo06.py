#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import re

if re.search('\\\\','i love one nee\dle') is not None:
   print('match it')
else:
   print('not match')
