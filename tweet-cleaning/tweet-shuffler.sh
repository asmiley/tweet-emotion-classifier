#!/bin/bash

# Append happy and sad tweets into a new file
cat ./happy/happy.clean >> HAPPYSAD &&
cat ./sad/sad.clean >> HAPPYSAD &&

# Randomize order of tweets
shuf HAPPYSAD --output=HAPPYSAD &&

# Print total number of tweets
printf "Number of lines: "
wc -l HAPPYSAD &&

# Divide into TEST, DEV, and TRAIN
# Start by creating a copy of the file as the training file
echo "Dividing data into TRAIN, DEV, and TEST"

# Split of 20% into the DEV file
split -l $[ $(wc -l HAPPYSAD |cut -d" " -f1) * 80 / 100 ] HAPPYSAD 8020 &&
mv 8020aa HAPPYSAD.TRAIN &&
rm -f 8020ac &&
# Splite half of the DEV file into TEST, so that both are 10% of the original file
split -l $[ $(wc -l 8020ab |cut -d" " -f1) * 50 / 100 ] 8020ab 5050 &&
rm -f 8020ab &&
mv 5050aa HAPPYSAD.DEV &&
mv 5050ab HAPPYSAD.TEST &&
rm -f 5050ac
echo "Done!"
