import json
import unirest
from nltk.corpus import words
import QueryParsing
import FindCommonWords
import sys
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

def checkJson(m):
		try:
			jsonObj = json.loads(m)
		except ValueError, e:
			return False
		return True

similarWords = "files\\inflectionalWords.txt"
fe1 = open(similarWords, 'w')
derivatives =  "files\\derivativeWords.txt"
fe2 = open(derivatives, 'w')
termsQueries = "files\\queries_terms.txt"

# code for generating query terms file queries_term.txt
#fe = open(termsQueries, "w")
#queryToken = QueryParsing.fetchQueryTokenized()
#querywords = set()
#for q in queryToken:
#		for t in queryToken[q]:
#			t = t.lower()
#			if not FindCommonWords.isCommon(t) and (t in words.words()):
#				querywords.add(t)
#for t in querywords:
# 	fe.write(t + " ")
#fe.close()

# reading the query terms from the file generated:
qt1 = open(termsQueries, 'r')
for string in qt1:
		terms = string.split()
qt1.close()

for each in terms:
		#print each
		inflectional = set()
		derivational = set()
		response = unirest.get("https://wordsapiv1.p.mashape.com/words/" + each,
		headers={
			"X-Mashape-Key": "tju4Z6vvqBmshqOvvJ0uVyjYNIhXp10qdAJjsnms5t3DtGHpPb",
			"Accept": "application/json" })

		if not checkJson(response.raw_body):
			continue
		objectJson = json.loads(response.raw_body)
		resAtt = u'results'
		if resAtt in objectJson:
			for result in objectJson["results"]:
				synonymAtt = u'synonyms'
				alsoAtt = u'also'
				similarAtt = u'similarTo'
				derivativAtt = u'derivation'
				if alsoAtt in result:
					for content in result[alsoAtt]:
						if not ' ' in content:
							inflectional.add(content)
				if similarAtt in result:
					for content in result[similarAtt]:
						if not ' ' in content:
							inflectional.add(content)
				if synonymAtt in result:
					for content in result[synonymAtt]:
						if not ' ' in content:
							inflectional.add(content)
				if derivativAtt in result:
					for content in result[derivativAtt]:
						if not ' ' in content:
							derivational.add(content)

		fe1.write(each)
		for content in inflectional:
				fe1.write(" ")
				fe1.write(content)
		fe1.write('\n')
		fe2.write(each)
		for content in derivational:
				fe2.write(" ")
				fe2.write(content)
		fe2.write('\n')

fe1.close()
fe2.close()
