#!/bin/sh

set -x

rsync -av --delete . randix_ncmx@ssh.phx.nearlyfreespeech.net:.
