#!/bin/sh

src=$1
echo $src

./cleanhtml.sh

cat head.txt index.txt tail.txt | sed "s;{SRC};$src;g" > index.html

cd travel; ./gen.sh $src
