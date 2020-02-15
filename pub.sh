#!/bin/sh

set -x

rsync -av --delete . randix_randix@ssh.phx.nearlyfreespeech.net:.
