#!/bin/bash
bigvar=$(echo $1 | tr 'a-z' 'A-Z')

echo "Janitor is cleaning!"
for f in *.txt;
do
    # Create a file with only a single tweet on each line
    awk '{FS="\t"}; {print $5" "$6" "$7" "$8" "$9" "$10}' $f >> $1.dirty
    echo "$f has been cleaned"
done &&
# Remove any line containing RT (retweets)
echo "Taking out some trash"
sed -i '/RT /d' $1.dirty &&
# Clean tweets, see janitor.py for more information
echo "Scrubbing the tweets. This could take a while!"
python tweet-soap.py $1.dirty $1.cleaner $1 &&
# Remove tweets with less than 3 words
echo "Taking out some more trash"
#awk '{"NF>=3"}; {print}' $1.cleaner > $1.clean &&
grep -P '\w+\s+\w+\s+\w+\s+\w+' $1.cleaner > $1.clean &&
# Remove duplicates
echo "So much trash!"
sort -u -o $1.clean $1.clean &&
# Randomize order of tweets
echo "Tidying up the place"
awk -i inplace -v var=$bigvar '{OFS="\t"}; {FS="\t"}; {print NR, var, $1}' $1.clean &&
# Remove previously created file
rm -f $1.dirty
rm -f $1.cleaner
echo "Clean!"