import math
import sys
import os, io
import operator
import QueryParsing
import relevanceFinder
import json
import re

finalTokenCount={}
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")
relevance_info_file = "cacm.rel"

def fetchBM25Score(nk,fi,qfi,dl,r,R):
		k1=1.2
		b=0.75
		k2=100
		score=0.0
		count = 0
		if fi==0:
			score=0.0
		else:
			K=k1*((1-b)+b*float(dl)/float(avdl))
			c1 = ((r + 0.5) / (R - r + 0.5)) / ((nk - r + 0.5) / (N - nk - R + r + 0.5))
			#c1=float(N-nk+0.5)/float(nk+0.5)
			c2=float((k1+1)*fi)/float(K+fi)
			c3=float((k2+1)*qfi)/float(k2+qfi)
			score=math.log(c1)*c2*c3
		return score
	
def findTheScores(Index1gram):
		tokenCount=0
		for term in Index1gram:
				indexList=Index1gram[term]
				for each in indexList:
					documentId=each[0]
					termFrequency=each[1]
					global finalTokenCount
					if finalTokenCount.has_key(documentId):
						finalTokenCount[documentId]=finalTokenCount[documentId]+termFrequency
						tokenCount=tokenCount+termFrequency
					else:
						finalTokenCount[documentId]=termFrequency
						tokenCount=tokenCount+termFrequency
		global N
		N=len(finalTokenCount.keys())
		global avdl
		avdl=tokenCount/N
		
		
# function to calculate ri values
def ri_value(index_value, relevance_info_qid):
    ri = 0
    for each in index_value:
        if each[0] in relevance_info_qid:
            ri += 1
    return ri
	
 
def writeToFile(SCoreOfDocument,queryid,output_directory):
		score_per_query=sorted(SCoreOfDocument.items(),key=operator.itemgetter(1),reverse=True)[:100]
		rankPrint=1  
		file=open(resultFolder+"query"+queryid.zfill(2) + "-" + output_directory +".txt",'w')
		for doc in score_per_query:
				file.write(str(queryid)+ " "+ "Q0 " +doc[0]+ " " +str(rankPrint).zfill(2)+ " " +str(doc[1])+ " " + output_directory +"\n")
				rankPrint+=1
		file.close()

def main(input_directory, output_directory,indexFile):
			global resultFolder
			resultFolder= "results\\" + output_directory + "\\"

			#index = indexer.indexer()
			index_filename=  "InvertedIndex\\" + indexFile
			
			# write the index to a file:
			#with io.open(index_filename, 'w', encoding='utf-8') as file:
			#		file.write(unicode(json.dumps(index,sort_keys=True)))
					
			# read the index file as Index1gram:		
			with open(index_filename) as data_file:
				Index1gram = json.load(data_file)
			
			# finding value for capital R:
			relevance_info = {}
			capital_r_value = {}
			for i in xrange(1, 65):
				relevance_info[i] = []
			with open(relevance_info_file, 'r') as f:
				reading_file = f.readlines()
				for val in reading_file:
					elements_list = val.split(" ")
					relevance_info[int(elements_list[0])] += [elements_list[2]]

				for key in relevance_info:
					count = 0
					for value in relevance_info[key]:
						count += 1
					capital_r_value[key] = count
			
			
			
			# calculate scores:	
			findTheScores(Index1gram)
			#if input_directory == "cacm.query.txt":
			#	fetchToeknsFromQueries = QueryParsing.fetchQueryTokenized() 
			#else:	
			fetchToeknsFromQueries = QueryParsing.fetchTokens2(input_directory)
			for key in fetchToeknsFromQueries:
						tokensInThisQuery = fetchToeknsFromQueries[key]
						newlist = tokensInThisQuery.split(" ")
						queryId = key + 1
						SCoreOfDocument={}
						#eachTermSet=list(set(tokensInThisQuery))
						for eachTerm in newlist:
							if Index1gram.has_key(eachTerm):
								indexList=Index1gram[eachTerm]
								df=len(indexList)
								freqOfQuery=newlist.count(eachTerm)
								for each in indexList:
									documentID=each[0]
									documentName=str(documentID)
									documentLength=finalTokenCount[documentID]
									docTFValue=each[1]
									ri = ri_value(indexList, relevance_info[queryId])
									score_per_term=fetchBM25Score(df,docTFValue,freqOfQuery,documentLength,ri,capital_r_value[queryId])
									if SCoreOfDocument.has_key(documentName):
										SCoreOfDocument[documentName]=SCoreOfDocument[documentName]+score_per_term
									else:
										SCoreOfDocument[documentName]=score_per_term
							writeToFile(SCoreOfDocument,str(queryId),output_directory)			


if __name__ == '__main__':
		 input_directory = sys.argv[1]
		 output_directory = sys.argv[2]
		 indexFile = sys.argv[3]
		 main(input_directory, output_directory,indexFile)
