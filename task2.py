from bs4 import BeautifulSoup
#import urllib.
import os
import re
from operator import itemgetter

#creating folders fr storing indexes and token counts:
try:
    dir2 = 'CountTokens'
    os.mkdir(dir2)
except OSError as err:
    print("Tokens folder exists")

#creating folders fr storing indexes and token counts:	
try:
    dir1 = 'InvertedIndex'
    os.mkdir(dir1)
except OSError as err:
    print("indexes folder exists")

	

def create_InvertedIndex(index,tokens,docId):
    #inputSet = set(tokens)
    for tOken in set(tokens):
	    # building an inverted index:
        t = (docId, tokens.count(tOken))
        if tOken not in index:
            index[tOken] = [t]
        else:
            l = index[tOken]
            l.append(t)
            index[tOken] = l
    return index

	
def SortInverteList(input_index):
    for key in input_index:
			# sort the index lexicographically based on term.
			l = input_index[key]
			# reverse =True
			l.sort(key=itemgetter(1),reverse=True)
			input_index[key] = l
    return input_index

	
def generateUnigrams(text):
    # generating unigrams by simply splitting the text.
    tokens = text.split()
    return tokens


def generateBigrams(tokens):
    bigramList = list()
	# generating a list of bigrams by combining 2 unigrams:
    for i in range(len(tokens) -1):
        bigramList.append(tokens[i] + " " + tokens[i+1])
    return bigramList


def generateTrigrams(tokens):
    trigramList = list()
	# generating a list of trigrams by combining 3 unigrams:
    for i in range(len(tokens) -2):
        trigramList.append(tokens[i] + " " + tokens[i+1] + " " + tokens[i+2])
    return trigramList


def writeListToFile(dir,file,iindex):
    f = open(os.path.join(dir,file+".txt"),"w")
	# write the output file 
    for tOken in iindex:
			f.write(tOken + " : " + str(iindex[tOken]) + "\n")
			f.flush()
    f.close()

	


def main():
    UnigramTokens = {}
    BigramTokens = {}
    TrigramTokens = {}
    InvertedUnigram = {}
    InvertedBigram = {}
    InvertedTrigram = {}
    counter = 1
    dirList=[]
    dirList=os.listdir("htmls/corpus/")
    for file in dirList:
			f1=open("htmls/corpus/"+file,"r")
			bodytext = f1.read()
        
			# generate unigrams, bigrams and trigrams:
			unigram_tokens = generateUnigrams(bodytext)
			bigram_tokens = generateBigrams(unigram_tokens)
			trigram_tokens = generateTrigrams(unigram_tokens)
		
			print(counter)
			docId = "D"+str(counter)
			# generate unigram, bigram and trigram indexes:
			InvertedUnigram = create_InvertedIndex(InvertedUnigram,unigram_tokens,docId)
			InvertedBigram = create_InvertedIndex(InvertedBigram,bigram_tokens,"D"+str(counter))
			InvertedTrigram = create_InvertedIndex(InvertedTrigram,trigram_tokens,"D"+str(counter))
		
			# sort the unigram , bigram and trigram indexes.
			InvertedUnigram = SortInverteList(InvertedUnigram)
			InvertedBigram = SortInverteList(InvertedBigram)
			InvertedTrigram = SortInverteList(InvertedTrigram)
		
			# generate token counts for the 3 indexes:
			UnigramTokens[docId] = len(set(unigram_tokens))
			BigramTokens[docId] = len(set(bigram_tokens))
			TrigramTokens[docId] = len(set(trigram_tokens))

			counter += 1
			f1.close()

	# write the index and token count list to files:	
    writeListToFile(dir1, "InvertedUnigram", InvertedUnigram)
    writeListToFile(dir2, "unigram_token_count", UnigramTokens)
    del InvertedUnigram
    del UnigramTokens

    writeListToFile(dir1, "InvertedBigram", InvertedBigram)
    writeListToFile(dir2, "bigram_token_count", BigramTokens)
    del InvertedBigram
    del BigramTokens
   
    writeListToFile(dir1, "InvertedTrigram", InvertedTrigram)
    writeListToFile(dir2, "trigram_token_count", TrigramTokens)
    del InvertedTrigram
    del TrigramTokens

main()


