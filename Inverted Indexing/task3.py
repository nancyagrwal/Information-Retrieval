from bs4 import BeautifulSoup
#import urllib.
import os
import re
from operator import itemgetter

try:
    dir1 = 'TermFrequency'
    os.mkdir(dir1)
except OSError as err:
    print("TermFrequency folder exists")

try:
    dir2 = 'DocFrequency'
    os.mkdir(dir2)
except OSError as err:
    print("DocFrequency folder exists")

def generateTF(index):
    termFreqLst = {}
    for tOken in index:
	        # find the term frequency in an index:
			count = 0
			list1 = index[tOken]
			for t in list1:
				count = count + t[1]
			termFreqLst[tOken] = count
    termFreqLst = sorted(termFreqLst.items(), key=itemgetter(1), reverse=True)
    return termFreqLst

	
def generateDC(index):
		docFreqList = {}
		for tOken in index:
			list1 = index[tOken]
			id = []
			# find the doc frequency :
			for tuple in list1:
				id.append(tuple[0])
			length = len(id)	
			docFreqList[tOken] = (id,length)
		docFreqList = sorted(docFreqList.items(), key=itemgetter(0))
		return docFreqList

		
def writeTF(dir,file,termFreqLst):
    f = open(os.path.join(dir, file + ".txt"), "w")
    for k,v in termFreqLst:
        f.write(k + " : " + str(v) + "\n")
        f.flush()
    f.close()

	
def writeDF(dir, file, docFreqList):
    f = open(os.path.join(dir, file + ".txt"), "w")
    for k,v in docFreqList:
        f.write(k + " : " + str(v[0]) + " : " + str(v[1]) + "\n")
        f.flush()
    f.close()

	
def returnIndexes(directory,fileName):
    index={}
    with open(os.path.join(directory,fileName),"r") as f:
        for line in f:
            line=line.replace("\n",'')
            line=line.split(":")
            line[1]=line[1].replace('[(','')
            line[1]=line[1].replace(')]','')
            line[1]=line[1].replace('(','')
            tuplesTok=line[1].split('),')
            list1=[]
            for tup in tuplesTok:
                newLine=tup.split(',')
                docId=newLine[0]
                count=int(newLine[1])
                tuple1=(docId,count)
                list1.append(tuple1)
                
            index[line[0]]=list1
    return index

	

def main():
 
		unigram_index=returnIndexes("InvertedIndex","InvertedUnigram.txt")
		termFreqUnigram = generateTF(unigram_index)
		writeTF(dir1, "termFreqUnigram", termFreqUnigram)
		docFreqUnigram = generateDC(unigram_index)
		writeDF(dir2,"docFreqUnigram",docFreqUnigram)

		del termFreqUnigram
		del docFreqUnigram

		bigram_index=returnIndexes("InvertedIndex","InvertedBigram.txt")
		termFreqBigram = generateTF(bigram_index)
		writeTF(dir1, "termFreqBigram", termFreqBigram)
		docFreqBigram = generateDC(bigram_index)
		writeDF(dir2,"docFreqBigram",docFreqBigram)

		del termFreqBigram
		del docFreqBigram

		trigram_index=returnIndexes("InvertedIndex","InvertedTrigram.txt")
		termFreqTrigram = generateTF(trigram_index)
		writeTF(dir1, "termFreqTrigram", termFreqTrigram)
		docFreqTrigram = generateDC(trigram_index)
		writeDF(dir2,"docFreqTrigram",docFreqTrigram)

		del termFreqTrigram
		del docFreqTrigram

def generateStopList():
  fr=[]
  priority=1
  tokens=[]
  c=0
    
  with open("TermFrequency/termFreqUnigram.txt","r") as f:
      for line in f:
        tokens.append(line)
        c+=int(line.split(':')[1])
  priority=1
  file=open("Stoplist.txt","w")
  for tOken in tokens:
    tf=float(tOken.split(":")[1])
    p5=float(tf/c)
    if( p5 > 0.001):
      file.write(tOken.split(":")[0]+"\n")
  file.flush()

main()
generateStopList()

