#!/bin/sh

src=$1

../cleanhtml.sh
cat ../head.txt index.txt        ../tail.txt | sed "s;{SRC};$src;g" > index.html
cat ../head.txt jeep-trailer.txt ../tail.txt | sed "s;{SRC};$src;g" > jeep-trailer.html

