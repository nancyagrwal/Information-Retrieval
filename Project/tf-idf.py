import math
import sys
import os, io
import operator
import QueryParsing
import json
import re

finalTokenCount={}
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

def tf_IdfScore(df,docTFValue,documentLength):
		tfValue=float(docTFValue)/float(documentLength)
		idfValue=float(math.log(N/df))
		score=float(tfValue)*float(idfValue)
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
				resultFolder="results\\" + output_directory + "\\"

				#index = indexer.indexer()
				index_filename= "InvertedIndex\\" + indexFile 
				
				# write the index to a file:
				#with io.open(index_filename, 'w', encoding='utf-8') as file:
				#		file.write(unicode(json.dumps(index,sort_keys=True)))
						
				# read the index file as Index1gram:		
				with open(index_filename) as data_file:
					Index1gram = json.load(data_file)
					
				# calculate scores:	
				findTheScores(Index1gram)
				#if input_directory == "cacm.query.txt":
				#	fetchToeknsFromQueries = QueryParsing.fetchTokens2("originalQuery.txt") 
				#else:	
				fetchToeknsFromQueries = QueryParsing.fetchTokens2(input_directory)
				for key in fetchToeknsFromQueries:
							tokensInThisQuery = fetchToeknsFromQueries[key]
							#print "tokens are....." , tokensInThisQuery
							newlist = tokensInThisQuery.split(" ")
							queryId = key + 1
							SCoreOfDocument={}
							#eachTermSet=list(set(tokensInThisQuery))
							#print "eachtermset...." , eachTermSet
							for eachTerm in newlist: # query terms of each query
								#print "term is......." , eachTerm
								if Index1gram.has_key(eachTerm):
									indexList=Index1gram[eachTerm]
									#print "indexList is......." , indexList
									df=len(indexList)
									#print "document freq is........." , df
									for each in indexList:
										documentID=each[0]
										documentName=str(documentID)
										documentLength=finalTokenCount[documentID]
										docTFValue=each[1]
										score_per_term=tf_IdfScore(df,docTFValue,documentLength)
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
