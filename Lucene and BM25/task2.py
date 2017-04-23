__author__ = 'Nancy'

import sys
from collections import OrderedDict
import math
import operator

corpus_dict = {}
c = 0

#file_inputFile = "C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\input\\unigram_index.txt";
file_inputFile = "input\\unigram_index.txt";
file_input = open(file_inputFile , "r")

#outputFile = "C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\output\\results_eval.txt";
outputFile = "output\\results_eval.txt";
maximum = 100
qr = open(outputFile, "w")
system_name='Nancy'

qr.write("id        Q0       doc_id      rank        BM25_forScore       system_name"+"\n")
given_queries = ['global warming potential','green power renewable energy','solar energy california','light bulb bulbs alternative alternatives']

for l in file_input:
    c = l.strip().split(":")
    term = c[0]
    non_term = c[1]
    term=term.replace(' ','')
    term=term.replace("\n","")
    term=term.replace("'","")
	
	# reading the unigram index file:
    non_term=non_term.replace('[','')
    non_term=non_term.replace(']','')
    non_term=non_term.replace('(','')
    non_term=non_term.replace('), ','#')
    non_term=non_term.replace(')','')
    non_term=non_term.replace(' ','')
    non_term=non_term.replace('D','')
    non_term=non_term.replace("'",'')
	
    keyValPair=non_term.split('#')
    dictionary1 = {}
    for k in keyValPair:
			key = int(k.split(",")[0])
			value = int(k.split(",")[1])
			# generating key value pairs of non term and putting them in the dictionary.
			dictionary1[key] = value
    
    if term not in corpus_dict:
			corpus_dict[term] = dictionary1

length = len(corpus_dict)			
print "length of dictionary is " , length
new_dict = {}
inBetweenLen = 0

for wrd in corpus_dict:
		countDoc = corpus_dict[wrd]
		for d in countDoc:
			if d not in new_dict:
				new_dict[d] = countDoc[d]
			else:
				new_dict[d] += countDoc[d]

for key in new_dict:
		inBetweenLen += new_dict[key]
		
# counting the total number of keys:		
allKeys = new_dict.__len__()

id = 0
for q in given_queries:
    id += 1
    qTerms = q.split(" ")
    # term_docs is a dict of term and docs it occurs in
    term_docs = {}
    for w in qTerms:
        if w in corpus_dict:
            countDoc = corpus_dict[w]
            docs_term = set()
            for dc in countDoc:
                docs_term.add(dc)
            term_docs[w] = docs_term
        else:
            term_docs[w] = None
 
    dict_bm25 = {}
    count_dict = {}
    # count_dict is dict of term key and value is number of occurances in entire corpus
    for wrd in qTerms:
        c = 0
        wrd=wrd.replace(' ','')
        wrd=wrd.replace('\n','')
        wrd=wrd.replace("'","")        
        if wrd in corpus_dict:
				countDoc = corpus_dict[wrd]
				for crd in countDoc:
					c += countDoc[crd]
        else:
				c = 0
        count_dict[wrd] = c

    k1 = 1.2
    k2 = 100
    dl = len(q)
    b = 0.75
    ab = inBetweenLen/float(allKeys)
    set_docs = set()
    for wrd in qTerms:
			docs = term_docs[wrd]
			for d in docs:
				set_docs.add(d)

    for d in set_docs:
		arg = new_dict[d] / float(ab)
		forScore = 0
		K = (b * arg) + (k1 * (1-b)) 
		for w in qTerms:
		    i = 0
		    P = 0
		    wCount = qTerms.count(w)
		    n = (i + 0.5) / (P - i + 0.5)
		    countDoc = corpus_dict[w]
		    if d in countDoc:
				  ifd = countDoc[d]
		    else:
				  ifd = 0
		    c1 = (k1+1) * ifd	  
		    first = c1 /(K + ifd)
		    c2 = (k2 + 1) * wCount
		    second = c2 / (k2 + wCount)
	        third_nr = (i + 0.5) / (P - i + 0.5)
			# find third dn:
		newLen = len(term_docs[w])
		c3 = (len(new_dict) - len(term_docs[w]))
	        third_dn = (newLen - i + 0.5) / float (c3 - P + i + 0.5)
		# printing:
		if (third_nr > 0 and third_dn > 0) or (third_nr < 0 and third_dn < 0):
				forScore += (math.log(third_nr/third_dn) * second * first)
		else:
				forScore += 0
		dict_bm25[d] = forScore
		
    # ordering the dictionary:
    top_25_dict = OrderedDict(sorted(dict_bm25.items(), key=operator.itemgetter(1), reverse=True)[:maximum])
    rank = 1
    #fileName = "C:\\Users\\nancy\\Desktop\\NancyAgrawal_IR_HW4\\output\\" + q.replace(" ",'_')
    fileName = "output\\" + q.replace(" ",'_')
    fileName+=".txt"
    queryFile=open(fileName,"w")
    for elem in top_25_dict.keys():
        queryFile.write(str(id) + "        " + "Q0" + "       " + str(elem) + "      " + str(rank) + "      " + str(top_25_dict[elem]) + "      " + str(system_name))
        rank += 1
        queryFile.write("\n")
    append_l = "***************************************************************************************" + "\n"
    queryFile.write(append_l)
    queryFile.close()







