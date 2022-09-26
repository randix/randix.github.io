#!/usr/bin/env python3

import os
import re
import sys

srcpath = sys.argv[1]
print(srcpath)

head = open("../head.txt").read()
tail = open("../tail.txt").read()

files = []
rawlist = open("filelist.txt").readlines()
for line in rawlist:
  files.append(line.strip())
  
home = '<a href="{SRC}index.html">home</a> &nbsp;'
up = '<a href="{SRC}travel/index.html">up</a> &nbsp;'

for i in range(len(files)):
  if i == 0:
    prev = "jeep-trailer.html" 
  else: 
    prev =  re.sub('.txt', '.html', files[i-1])
  if i == len(files)-1:
    next = None
  else: 
    next = re.sub('.txt', '.html', files[i+1])

  prev = '<a href="{SRC}travel/' + prev + '">previous</a> &nbsp;' 
  if next != None:
    next = '<a href="{SRC}travel/' + next +'">next</a>'
  
  text = open(files[i]).read()

  if next == None:
    html = head + home + up + prev +        text + '<p/>' + prev +        tail
  else:
    html = head + home + up + prev + next + text + '<p/>' + prev + next + tail

  html = re.sub('{SRC}', srcpath, html)

  f = os.path.splitext(files[i])[0]+'.html'
  open(f, 'w').write(html)

