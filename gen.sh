#!/bin/sh
set -x

src=$1
echo $src

rm *.html
cat head.txt index.txt tail.txt | sed "s;{SRC};$src;g" > index.html

rm travel/*.html
cat head.txt travel/index.txt                  tail.txt | sed "s;{SRC};$src;g" > travel/index.html
cat head.txt travel/jeep-trailer.txt           tail.txt | sed "s;{SRC};$src;g" > travel/jeep-trailer.html
cat head.txt travel/220831-220904-home-cda.txt tail.txt | sed "s;{SRC};$src;g" > travel/220831-220904-home-cda.html
cat head.txt travel/220905-cda-devils-lake.txt tail.txt | sed "s;{SRC};$src;g" > travel/220905-cda-devils-lake.html

