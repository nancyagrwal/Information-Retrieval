import sys

# nonRelevantDocs = set([34, 35, 41, 46, 47, 50, 51, 52, 53, 54, 55, 56])
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

fileRelevance = sys.path[0] + "\\cacm.rel"
def docQueryRelevance(qn, fileName):
		if fileName[-5:] == ".html":
			fileName = fileName[:-5]
		fe = open(fileRelevance, 'r')
		dictRlevance = {}
		qn = str(qn)
	
		for i in range(1, 65):
			dictRlevance[str(i)] = set()
		for each in fe:
			eachList = each.split()
			retrievedQuery = eachList[0]
			fileNm = eachList[2]
			dictRlevance[retrievedQuery].add(fileNm)

		fe.close()

		if fileName in dictRlevance[qn]:
			return True
		else:
			return False

def retrievedQueryRelevance(qn):
		fe = open(fileRelevance, 'r')
		qn = str(qn)
		relCountDocs = 0
		for each in fe:
			eachList = each.split()
			retrievedQuery = eachList[0]
			if retrievedQuery == str(qn):
				relCountDocs += 1

		fe.close()
		return relCountDocs
	
	
def retrieveRelevantDocs():
	relDocs = set()
	for i in range(1,64):
			fe = open(fileRelevance, 'r')
			qn = str(i)
			for each in fe:
				eachList = each.split()
				retrievedQuery = eachList[0]
				retrievedDocId = eachList[2]
				if retrievedQuery == str(i):
					count=+1
					relDocs.add(retrievedDocId)

			fe.close()
	wordSet = set()
	k = next(iter(relDocs))
	number = k.split("-")[1].zfill(4)
	fe1 = open ("stemmedCorpus\\" + "CACM-" + number +".txt" , "r")
	for each in fe1:
		wordSet.add(each)

	return wordSet
#retrieveRelevantDocs()	

def findCount():
		totalCount =0
		for i in range(1,64):
			totalCount += retrievedQueryRelevance(i)
		print totalCount

#findCount()		
			
		


