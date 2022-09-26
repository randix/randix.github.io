#!/bin/sh

find . | egrep ".jpg|.jpeg" | sort | sed -e 's;^\.;<p/><img src="{SRC}travel/;' -e 's;$;" width="640"/>;' > photo.list

