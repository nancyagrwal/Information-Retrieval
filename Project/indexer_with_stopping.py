from bs4 import BeautifulSoup
import os, sys, io
import codecs
import json
import string
import re

directory =  sys.path[0] + "\\htmls\\"  # directory
common_words_file = sys.path[0] + "\\files\\common_words.txt"
index = {}

# function to open files in the corpus folder
def indexer():
			stopwords = stopwords_list(common_words_file)
			for each_file in os.listdir(directory):
					header, delimiter, footer = each_file.partition('.')
					opening_html = codecs.open(directory + each_file, 'r', 'utf-8')
					reading_html = opening_html.read()
					soup_var = BeautifulSoup(reading_html, "html.parser")
					text = soup_var.findAll(text=True)
					text_without_tags = filter(delete_tags, text)  # removing html tags from whole text using filter function
					item = string.replace(','.join(text_without_tags), '\n', ' ')
					item_filtered = string.replace(item, ':', ' ')
					filtered_item = string.replace(item_filtered, '-', ' ')
					head, sep, tail = filtered_item.partition(" PM ")
					head, sep, tail = (head + sep).partition(" AM ")
					text_without_punctuations = re.sub(r'[^\w\s|-]', r'', head + sep)  # removing punctuations using regex
					lower_case_text = text_without_punctuations.lower().encode('utf-8')  # case folding and encoding
					tokens = lower_case_text.split()
					for each_Word in tokens:
						if each_Word not in stopwords:
							if each_Word == "":
								continue
							elif each_Word != " ":
								if each_Word not in index:
									index[each_Word] = [[header, 1]]
								else:
									indexing(each_Word, header)
							else:
								pass
							
			index_filename= "InvertedIndex\\stoppedIndex.txt"
			# write the index to a file:
			with io.open(index_filename, 'w', encoding='utf-8') as file:
						file.write(unicode(json.dumps(index,sort_keys=True)))
			return index


def stopwords_list(filename):
    stopwords = []
    with open(filename, 'r') as f:
        for each_val in f.readlines():
            item = string.replace(each_val, '\n', '')
            stopwords.append(item)
    return stopwords
	
def delete_tags(text):
    if text.parent.name in ['style', 'script', '[document]', 'head']:
        return False
    else:
        return True


def indexing(term, filename):
    global index
    condition = False
    for value in index[term]:
        if value[0] == filename:
            condition = True
            value[1] += 1

    if condition == False:
        index[term].append([filename, 1])
		
indexer()