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
  
home = '<a href="{SRC}index.html"><span style="font-size:14px;">home</span></a> &nbsp;'
up = '<a href="{SRC}travel/index.html"><span style="font-size:14px;">up</span></a> &nbsp;'

for i in range(len(files)):
  if i == 0:
    prev = "jeep-trailer.html" 
  else: 
    prev =  re.sub('.txt', '.html', files[i-1])
  if i == len(files)-1:
    next = None
  else: 
    next = re.sub('.txt', '.html', files[i+1])

  prev = '<a href="{SRC}travel/' + prev + '"><span style="font-size:14px;">previous</span></a> &nbsp;' 
  if next != None:
    next = '<a href="{SRC}travel/' + next +'"><span style="font-size:14px;">next</span></a>'
  
  text = open(files[i]).read()

  if next == None:
    html = head + home + up + prev +        text + '<p/>' + prev +        tail
  else:
    html = head + home + up + prev + next + text + '<p/>' + prev + next + tail

  html = re.sub('{SRC}', srcpath, html)

  f = os.path.splitext(files[i])[0]+'.html'
  open(f, 'w').write(html)

