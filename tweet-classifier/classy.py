#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import regex as re
from collections import defaultdict

"""Open files"""
def openFileTrain(): ###Copy for train, dev, and test
    #Take a file and return a list of lines
    infileObject=open(str(sys.argv[1]+'.TRAIN'), "r")
    list_of_lines_train=infileObject.readlines()
    return list_of_lines_train

def openFileDev(): ###Copy for train, dev, and test
    #Take a file and return a list of lines
    infileObject=open(str(sys.argv[1]+'.DEV'), "r")
    list_of_lines_dev=infileObject.readlines()
    return list_of_lines_dev

def openFileTest(): ###Copy for train, dev, and test
    #Take a file and return a list of lines
    infileObject=open(str(sys.argv[1]+'.TEST'), "r")
    list_of_lines_test=infileObject.readlines()
    return list_of_lines_test


def getDict(list_of_lines):
    """

    """
    #Put each column in variable
    word_dict = defaultdict() #collections.defaultdict?
    indexCounter = 1 #move outside?
    for l in list_of_lines:
        myID, tag, tweet_text = l.split("\t")
        ####################
        word_list = tweet_text.split()
        #words = set(words)
        ####################
        for w in word_list:
            if w not in word_dict:
                word_dict[w] = indexCounter
                indexCounter +=1
    return word_dict


#call 3 times

def writeVectors(outfile, list_of_lines, word_dict):
    """

    """
    #Assign value of each column to a variable
    for l in list_of_lines:
        myID, tag, tweet_text = l.split("\t")
        words = tweet_text.split()
        words = set(words)
        tweet_index=[]

        if tag=="HAPPY":
            print>>outfile, "1",
            for w in words:
                if w in word_dict:
                    tweet_index.append(word_dict[w])
            tweet_index.sort()
            for i in tweet_index:
                print>>outfile, str(i)+":1.0",
            print>>outfile
        else:
            print>>outfile, "-1",
            for w in words:
                if w in word_dict:
                    tweet_index.append(word_dict[w])
            tweet_index.sort()
            for i in tweet_index:
                print>>outfile, str(i)+":1.0",
            print>>outfile

def main():

    print("Initializing...")
    trainOutfile=open("TRAIN.SVM", "w")
    devOutfile=open("DEV.SVM", "w")
    testOutfile=open("TEST.SVM", "w")

    print("Creating dictionary...")
    list_of_lines_train = openFileTrain()
    word_dict = getDict(list_of_lines_train)


    list_of_lines_dev = openFileDev()
    list_of_lines_test = openFileTest()


    print("Vectorizing...")
    writeVectors(trainOutfile, list_of_lines_train, word_dict)
    writeVectors(devOutfile, list_of_lines_dev, word_dict)
    writeVectors(testOutfile, list_of_lines_test, word_dict)
    print("Done!")

#Calling main:
if __name__ == "__main__":
    main()