import os
import indexer_with_stopping


directory = 'StemmedCorpus/'  # directory
index = {}
common_words_file = "files\\common_words.txt"


# function to open files in the corpus folder
def open_files():
		for each_file in os.listdir(directory):
			stopwords = indexer_with_stopping.stopwords_list(common_words_file)
			header, delimiter, footer = each_file.partition('.')
			doc_id = header
			open_file_obj = open(directory + each_file, 'r')  # opening file in a read mode
			read_file = open_file_obj.readline()  # reading file
			tokens = read_file.split()  # tokenizing the text
			for item in tokens:
				if item not in stopwords:
					if item == "":
						continue
					elif item != " ":
						if item not in index:
							index[item] = [[doc_id, 1]]
						else:
							indexing(item, doc_id)
					else:
						pass

			open_file_obj.close()  # closing the file
		index_filename= sys.path[0] + "InvertedIndex\\stoppedStemmedIndex.txt"
		# write the index to a file:
		with io.open(index_filename, 'w', encoding='utf-8') as file:
					file.write(unicode(json.dumps(index,sort_keys=True)))
		return index

		#saving_indexes_in_file(index)  # saving the output into file


# function to create indexes
def indexing(term, filename):
    global index
    condition = False
    for value in index[term]:
        if value[0] == filename:
            condition = True
            value[1] += 1

    if condition == False:
        index[term].append([filename, 1])


# function to save the output to a file
indexFileName = "InvertedIndex\\stoppedStemmedIndex.txt"
def saving_indexes_in_file(dictionary):
    file = open(indexFileName, 'w')  # opening a file in write mode
    file.write(str(dictionary))  # writing content to a file
    file.close()  # closing the file


# function call to open files and creating the respective indexes
open_files()
