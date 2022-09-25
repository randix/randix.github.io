#!/bin/sh

./gen.sh 'https://randix.net/'

cd travel
./gen.sh 'https://randix.net/'
./gen.py 'https://randix.net/'
cd ..

sftp randix_randix@ssh.phx.nearlyfreespeech.net << EOF
put *html
cd travel
lcd travel
put *html
EOF

