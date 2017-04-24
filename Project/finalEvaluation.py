import glob
import relevanceFinder
import os
import sys
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

# creating directories for evaluation heads:
dirList = []
dirList.append("Lucene")
dirList.append("BM25")
dirList.append("BM25_Derivatives")
dirList.append("TFIDF_Derivatives")
#dirList.append("BM25_Synonyms")
dirList.append("TFIDF_Synonyms")
dirList.append("Stop_BM25")
dirList.append("Stop_TFIDF")
dirList.append("TFIDF")
for DirName in dirList:
		outFileName = sys.path[0] + "\\evaluation\\" + DirName + "_Evaluation.txt"
		outKFileName = sys.path[0] + "\\evaluation\\" + DirName + "_PrecisionAtK.txt"
		fe = open(outFileName, 'w')
		fe.write("Query Rank Precision Recall\n")
		fek = open(outKFileName, 'w')
		fek.write("Query Pat5 Pat20\n")
		map = 0.0
		mrr = 0.0
		mk5 = 0.0
		mk20 = 0.0
		countQueries = 0
		
		os.chdir(sys.path[0] + "\\results\\" + DirName)
		
		for filename in glob.glob("*.txt"):
			queryNum = filename[5 : 7]
			openStream = open(filename, 'r')
			avgPrecision = 0.0
			reciPrecision = 0.0
			preAt5 = 0.0
			preAt20 = 0.0
			finalRelevance = 0.0
			recall = 0.0
			queryNum = queryNum.lstrip('0')
			#print queryNum
			# calculating total relevance from file relevanceFinder:   
			completeRel = float(relevanceFinder.retrievedQueryRelevance(queryNum))
			if completeRel == 0:
				continue
			else:
				countQueries += 1

			for each in openStream:
				eachList = each.split()
				quer = eachList[0]
				document = eachList[2]
				rank = float(eachList[3])
				relFlag = relevanceFinder.docQueryRelevance(queryNum, document)
				#print quer + " " + document + " " + str(rank)
					
				# if the documents are relevant to the query terms:
				if relFlag:
					finalRelevance += 1
					avgPrecision += finalRelevance / rank
					if reciPrecision == 0.0:
						reciPrecision = 1 / rank
					if completeRel > 0.0:
						recall = finalRelevance / completeRel
					else:
						recall = 0
				
				# finding precisions at 5 and 20:
				if rank == 5.0:
					preAt5 = finalRelevance / rank
				if rank == 20.0:
					preAt20 = finalRelevance / rank

				fe.write(str(queryNum) + " ")
				fe.write(str(int(rank)) + " ")
				fe.write(str(finalRelevance / rank) + " ")
				fe.write(str(recall) + "\n")

			if finalRelevance == 0.0:
				avgPrecision = 0.0
			else:
				avgPrecision /= finalRelevance

			fek.write(str(queryNum) + " ")
			fek.write(str(preAt5) + " ")
			fek.write(str(preAt20) + "\n")

			map += avgPrecision
			mrr += reciPrecision
			mk5 += preAt5
			mk20 += preAt20


			openStream.close()

		map /= countQueries
		mrr /= countQueries
		mk5 /= countQueries
		mk20 /= countQueries

		fe.write('\n') 
		fe.write( "map  " + str(map) + '\n')
		fe.write( "mrr  " + str(mrr) + '\n')
		fe.write( "mk5  " + str(mk5) + '\n')
		fe.write( "mk20 " + str(mk20) + '\n')
		fe.close()
		fek.close()

		print DirName
		print "  MAP = " + str(map)
		print "  MRR = " + str(mrr)
		print "  MK5 = " + str(mk5)
		print "  MK20= " + str(mk20)