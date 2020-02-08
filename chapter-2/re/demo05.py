#!/usr/bin/python3
#-* coding:UTF-8 -*-

import re

text_string = ['[重要的]今年第7号台风23日登陆广东东部沿海地区','上海发布车库监管通知：违规者暂停网签资格','[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']

regex = '^\[[重紧]..\]'

for line in text_string:
  if re.search(regex,line) is not None:
    print(line)
