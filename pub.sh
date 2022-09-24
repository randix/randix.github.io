#!/bin/sh
set -x

./gen.sh 'https://randix.net/'

sftp randix_randix@ssh.phx.nearlyfreespeech.net << EOF
put *html
cd travel
lcd travel
put *html
EOF

