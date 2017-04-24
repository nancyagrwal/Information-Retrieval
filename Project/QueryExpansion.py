import QueryParsing
import FindCommonWords
import sys
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code")

similarity =  "files\\inflectionalWords.txt"
fe1 = open(similarity, 'r')
derivative =  "files\\derivativeWords.txt"
fe2 = open(derivative, 'r')
similarDict = {}
derivativeDict = {}
for term in fe1:
		s = term.split()
		if(len(s) > 1):
			similarDict[s[0]] = s[1:]

for term in fe2:
		d = term.split()
		if(len(d) > 1):
			derivativeDict[d[0]] = d[1:]

fe1.close()
fe2.close()

# creating output files:
similarOut =  "queries\originalQueryExpandedWithSynonyms.txt"
s1 = open(similarOut, 'w')
derivativeOutput =  "queries\originalQueryExpandedWithDerivatives.txt"
s2 = open(derivativeOutput, 'w')
oOut =  "queries\originalQuery.txt"
s3 = open(oOut, 'w')
stoppedOut =  "queries\QueryWithoutStoppedWords.txt"
s4 = open(stoppedOut, 'w')
stopderivativeOut =  "queries\StoppedQueryExpandedWithDerivatives.txt"
s5 = open(stopderivativeOut, 'w')
# getting tokens from the query using QueryParsing class.
tokenizedQuery = QueryParsing.fetchQueryTokenized()
for term in tokenizedQuery:
		s1.write(str(term + 1) + " ")
		s2.write(str(term + 1) + " ")
		s3.write(str(term + 1) + " ")
		s4.write(str(term + 1) + " ")
		s5.write(str(term + 1) + " ")
		for term in tokenizedQuery[term]:
			s1.write(term.lower())
			s1.write(" ")
			s2.write(term.lower())
			s2.write(" ")
			s3.write(term.lower())
			s3.write(" ")
			if not FindCommonWords.isCommon(term):
				s4.write(term.lower())
				s4.write(" ")
				s5.write(term.lower())
				s5.write(" ")
			if term in similarDict:
				for sim in similarDict[term]:
					s1.write(sim)
					s1.write(" ")
			if term in derivativeDict:
				for der in derivativeDict[term]:
					s2.write(der)
					s2.write(" ")
					if not FindCommonWords.isCommon(term):
						s5.write(der)
						s5.write(" ")
		s1.write('\n')
		s2.write('\n')
		s3.write('\n')
		s4.write('\n')
		s5.write('\n')
	
s1.close()
s2.close()
s3.close()
s4.close()
s5.close()