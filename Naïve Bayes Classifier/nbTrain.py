
from __future__ import division
from math import log
import glob
import json
import re
import time
import sys


def freq_dictionary_pop(list_f):
        terms_freq = {}
        print "freq_dictionary_pop"
        for i in list_f:
            terms = i.split()
            for k in terms:
                terms_freq[k] = terms_freq.get(k,0) + 1
        return terms_freq

def total_freq_map(dict_temp_1,dict_temp_2):
        
        print "total_freq_map"
        allWordsDict = {}
        allWordsDict = dict_temp_1.copy()
        for i in dict_temp_2.keys():
            allWordsDict[i] = allWordsDict.get(i,0)+dict_temp_2[i]
        return allWordsDict

def list_file_data(file_path):

        print "list_file_data"
        list_f = []
        for i in file_path:
            file_read_data = open(i,'r')
            list_f.append(file_read_data.read())
        return list_f

def total_freq_find(inputD,wordsinputD):
        print "total_freq_find"
        termCount = 0
        for i in inputD.keys():
            if wordsinputD[i]<5:
                inputD.pop(i)
            else:
                termCount += inputD[i]
        return termCount,inputD

def main(fileInput,fileOutput):

            start_time = time.time()

            print "*************************main call laplace smooothing*******************************"

            listOfNeg = []  # list of negative
            listOfPos = []  # list of positive
            dictNeg = {}
            dictPos = {}
            negative_train_files  = glob.glob(fileInput+'/neg/*.txt') # training files
            postive_train_file  = glob.glob(fileInput+'/pos/*.txt')   # training files
            listOfNeg = list_file_data(negative_train_files)   # list from training files
            listOfPos = list_file_data(postive_train_file)      # iist from training files" 
            dictNeg = freq_dictionary_pop(listOfNeg)
            dictPos = freq_dictionary_pop(listOfPos)
            allWordsDict = total_freq_map(dictNeg,dictPos)

            for i in allWordsDict.keys():
                dictPos[i] = dictPos.get(i,0)
                dictNeg[i] = dictNeg.get(i,0)
            print "********************************************************************"
            print "********************************************************************"
            print "total number of words:", allWordsDict.__len__()
            print "negative words length",dictNeg.__len__()
            print "positive words length",dictPos.__len__()
            print "********************************************************************"
            print "*******************************************************************"
            negCountTotal = 0
            posCountTotal = 0
            negCountTotal,dictNeg = total_freq_find(dictNeg,allWordsDict)
            posCountTotal,dictPos = total_freq_find(dictPos,allWordsDict)
            allWordsDict = {}
            allWordsDict = total_freq_map(dictNeg,dictPos)
            print "***********************************************************************"
            print "negative_words length",dictNeg.__len__()
            print "positive_words length-> length",dictPos.__len__()

            probNeg = {}
            probPos = {}
            totalLength = allWordsDict.__len__()
            print "total words:", totalLength
            print "total negative words:", negCountTotal
            print "total positive word:", posCountTotal
            print "****************************************************************************"
            print "***************************************************************************"
            
            print "###################################Smooothing_normal###################################"
            
            for i in dictNeg.keys():
                probNeg[i] = (dictNeg[i]+1)/(negCountTotal+totalLength)

            for i in dictPos.keys():
                probPos[i] = (dictPos[i]+1)/(posCountTotal+totalLength)

            print "print_print",probNeg
            print "********************************ends*************************************************"
            finalProbList = [probNeg,probPos]
            model_file = open(fileOutput,"w")
            json.dump(finalProbList,model_file)

            end_time = time.time()  
            print "total time taken::::",end_time-start_time


if __name__ == '__main__':
    input_dir = sys.argv[1]
    output_model = sys.argv[2]
    main(input_dir, output_model)
