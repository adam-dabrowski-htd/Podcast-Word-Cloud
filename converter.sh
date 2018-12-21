#!/bin/bash

set -eux

FILE=$(basename $1)

wget -O $FILE $1

echo "Converting to flac for cloud services"
ffmpeg -i $FILE -ar 16000 $2
