#!/bin/bash
# First, sort happy tweets into tweet-cleaning/happy
# And sad tweets into tweet-cleaning/sad
# Then run this script to automate the rest of the process

# Doing some housework
rm -f ./tweet-cleaning/HAPPYSAD
rm -f ./tweet-cleaning/HAPPYSAD.DEV
rm -f ./tweet-cleaning/HAPPYSAD.TEST
rm -f ./tweet-cleaning/HAPPYSAD.TRAIN &&

# Clean and prepare tweets
cd tweet-cleaning/happy
./janitor.sh happy &&
cd ../sad
./janitor.sh sad &&
cd ..
./tweet-shuffler.sh &&

# Build classifier
cd ../tweet-classifier
python classy.py ../tweet-cleaning/HAPPYSAD