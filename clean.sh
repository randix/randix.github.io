#!/bin/sh

rm -f ipad-*.html tech-*.html arete-*.html
rm -f technical.html arete.html index.html

find . -name .DS_Store -print0 | xargs -0 rm
