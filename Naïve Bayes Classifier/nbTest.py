
import sys
from math import log
import json
from collections import OrderedDict
import os
import operator
import glob
from operator import itemgetter


dicttestData = {}
predictDict = {}
posNegList = []
POSITIVE = []
NEGATIVE = []
posNegDict = dict()
negPosdict = dict()
posTop =[]
negTop = []


def top20_print(first_twenty):
            top = 0
            for key,value in first_twenty.iteritems():
                top = top+1
                print key,value,'\n'
                if top == 20:
                     break
    
def main(modelFile, input_directory, predicFile):    
            fileListOfTest = []
            print input_directory
            with open(modelFile) as f:
                try:
                    modelData = json.load(f)
                except ValueError:
                    modelData = []

            count_pos_terms = modelData[1]
            count_neg_terms = modelData[0]

            for key, value in count_pos_terms.iteritems():
                posNegDict[key] = log(value) - log(count_neg_terms.get(key))

            for key, value in count_neg_terms.iteritems():
                negPosdict[key] = log(value) - log(count_pos_terms.get(key))

            dictNew= OrderedDict(reversed(sorted(posNegDict.items(), key=itemgetter(1))))
            print "list of the 20 terms with the hig (log) ratio of positive - negative weight...\n"
            top20_print(dictNew)

            print "************************************************************************"
            
            dictNewOther= OrderedDict(reversed(sorted(negPosdict.items(), key=itemgetter(1))))
            print "list of the 20 terms with the hig (log) ratio of negative - positive weight... \n"
            top20_print(dictNewOther)
            
            print "***************************************************************************"
            
            pathFile = ""

            for directoryName, subList, fileList in os.walk(input_directory):
                for fname in fileList:
                    fileListOfTest.append(directoryName+"/"+fname)
            print fileListOfTest
            for i in fileListOfTest:
                input_file = open(i,'r')

                dicttestData[i] = input_file.read().replace('\n',' ')
                c = 0
                posCUMProb = 0.0
                negCUMProb = 0.0
                words = dicttestData[i].split()

                for k in words:
                    posCUMProb += log(count_pos_terms.get(k,1))
                    negCUMProb += log(count_neg_terms.get(k,1))
          

                predictDict[i] = [posCUMProb,negCUMProb]
                if posCUMProb > negCUMProb:
                    POSITIVE.append(i)
                else:
                    NEGATIVE.append(i)

                print "POSITIVE- LENGTH", len(POSITIVE)
                print "NEGATIVE- LENGTH", len(NEGATIVE)
                print "list length", len(predictDict)

            myFile = open(predicFile, 'a')
            myFile.write('{:>5}\t{:>5}\t{:>2}\t'.format("file-name","pos-score","neg-score"))
            for key, value in predictDict.iteritems():
                stringSen = " ".join(reversed(str(key).split('/')))
                myFile.write('{:>5}\t{:>5}\t{:>2}\t'.format(stringSen.split()[0],value[0],value[1]))
                myFile.write("\n")



if __name__ == '__main__':
     modelFile = sys.argv[1]
     input_directory = sys.argv[2]
     predicFile = sys.argv[3]
     main(modelFile, input_directory, predicFile)


