import re
import sys
from nltk.tokenize import regexp_tokenize 
#pip install -U nltk 

#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

def fetchOnlyRelevantDocTerms():
		queries = "InputFilesGiven\\cacm.query.txt"
		f = open(queries,'r')
		count = 0
		flag = False
		setQuery = {}
		for l in f:
			stringLine = l[:-1]
			if len(stringLine) == 0:
				continue
			elif (stringLine[0] == ' ' and len(stringLine) == 1) or stringLine[0] == '<':
				flag = False
				continue
				
			else:
				if not flag:
					setQuery[count] = ""
					setQuery[count] += stringLine
					flag = True
					count += 1
				else:
					setQuery[count - 1] += " "
					setQuery[count - 1] += stringLine
				
		finalList = {}
		for q in setQuery:
			pattern = '[\d]+[\.\,\d]*[\d]+\%?|\[\d+\]|[\w\-]+'
			finalList[q] = regexp_tokenize(setQuery[q], pattern)

		return finalList

def fetchQueryTokenized():
		queries = "InputFilesGiven\\cacm.query.txt"
		f = open(queries,'r')
		count = 0
		flag = False
		setQuery = {}
		for l in f:
			stringLine = l[:-1]
			if len(stringLine) == 0:
				continue
			elif (stringLine[0] == ' ' and len(stringLine) == 1) or stringLine[0] == '<':
				flag = False
				continue
				
			else:
				if not flag:
					setQuery[count] = ""
					setQuery[count] += stringLine
					flag = True
					count += 1
				else:
					setQuery[count - 1] += " "
					setQuery[count - 1] += stringLine
				
		finalList = {}
		for q in setQuery:
			pattern = '[\d]+[\.\,\d]*[\d]+\%?|\[\d+\]|[\w\-]+'
			finalList[q] = regexp_tokenize(setQuery[q], pattern)
		#print finalList
		return finalList

		
def fetchTokens2(inputfileName):
			queries = "queries\\" + inputfileName 
			f = open(queries,'r')
			count = 0
			setQuery = {}
			for l in f:
				stringLine = l[2: ]
				#print "stringLine is......." , stringLine
				setQuery[count] = ""
				setQuery[count] += stringLine
				count += 1
			#print "the query set is........." , setQuery	
			
			finalList = {}
			for q in setQuery:
				finalList[q] = setQuery[q]
			#print "finalList is............" , finalList
			return finalList
			#return setQuery

fetchQueryTokenized()