import sys
#sys.path.insert(0, "C:\\Users\\nancy\\Desktop\\code\\")

commonWordsFileName = sys.path[0] + "\\files\\common_words.txt"
def readCommonWords():
		f = open(commonWordsFileName, 'r')
		setCommonWords = set()
		# read the common_words file and store it in setCommonords set
		for string in f:
			setCommonWords.add(string[:-1]) 
		f.close()
		return setCommonWords

def isCommon(w):
		w = w.lower()
		commonWord = readCommonWords()
		return w in commonWord
