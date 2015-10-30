#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import regex as re
import sys
import urlparse

def cleanTweet(tweet, query_term):
    """
    """
    new_string = ''
    for i in tweet.split(): # remove urls, hashtag characters, and full @username mentions
        s, n, p, pa, q, f = urlparse.urlparse(i)
        if s and n:
            pass
        elif i[:1] == '@':
            pass
        elif i[:1] == '#':
            new_string = new_string.strip() + ' ' + i[1:]
        else:
            new_string = new_string.strip() + ' ' + i

    table = string.maketrans("","") # make a translation table
    new_string = re.sub("[^A-Za-z']+", ' ', new_string) # agressive and removes all non-alphanumeric (works only for latin-based and maybe only English)
    new_string = new_string.replace(" amp ", " ") # remove html code for ampersands($)
    new_string = new_string.lower() # lowercase entire tweet
    new_string = re.sub(r'(.)\1+', r'\1\1', new_string) # reduces any char repition of > 2 to 2.
    new_string = new_string.replace(query_term, " ") # take the original value used to collect tweets as a system argument, and remove it from tweets
    new_string = re.sub(r'(?<!\S)\S{1}(?!\S)', '', new_string)
    new_string = ' '.join(new_string.split()) # remove additional spaces

    return new_string


def main():
    with outfile as f:
        for line in infile:
            clean = cleanTweet(line, query_term)
            f.write(str(clean) + '\n')
    infile.close()
    outfile.close()

if __name__ == "__main__":
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    query_term = str(sys.argv[3])
    main()