#!/usr/bin/env python

import os
import glob
import re

# get the templates
hname = "head.html"
tname = "tail.html"
head = open(hname).read()
tail = open(tname).read()

def newer(on, nn):
  try:
    if os.stat(on)[8] > os.stat(nn)[8]:
      return True
  except:
    return True
  return False

def gen(name, html):
  global head, tail
  print(name)
  out = open(name, "w+")
  out.write(head)
  out.write(html)
  out.write(tail)
  out.close()

# make lists and the doc files
base = ["profile.html", "resume.html"]
for f in base:
  name = "base-"+f
  if newer(f, name) or newer(hname, name) or newer(tname, name):
    gen("base-"+f, open(f).read())

# SET the INDEX file....
index = "profile.html"

# generate the index file
if newer(index, "index.html"):
  gen("index.html", open(index).read())

