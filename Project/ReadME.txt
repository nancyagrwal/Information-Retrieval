To install unirest:
$ pip install unirest

to install nltk:
Run the Python interpreter and type the commands:
>>> import nltk
>>> nltk.download()

For indexing:

-> Using the indexer.py, the inverted index is generated for the base-runs, in file named "Index1gram.txt".
-> Using createDocsFromStem.py file, corpus documents are generated (from raw html documents) and saved into a folder named "stemmedCorpus". Using indexer_with_stopping.py, inverted index with stopping for un-stemmed corpus is generated in a file named, "stoppedIndex.txt". Using indexer_for_stemmed_corpus, inverted index with stopping for stemmed corpus is generated in a file named, "stoppedStemmedIndex.txt".

RETRIEVAL MODELS:

1) TFIDF:
python tf-idf.py <query-fileName> <output-folder> <index-filename>
1) To run TFIDF on original query set:
python tf-idf.py originalQuery.txt TFIDF index1gram.txt
The results are stored in TFIDF folder in results folder

2) To run TFIDF on originalQueryExpandedWithDerivatives.txt 
python tf-idf.py originalQueryExpandedWithDerivatives.txt TFIDF_Derivatives index1gram.txt
The results are stored in TFIDF_Derivatives folder in results folder

3)To run TFIDF on originalQueryExpandedWithSynonyms.txt
python tf-idf.py originalQueryExpandedWithSynonyms.txt TFIDF_Synonyms index1gram.txt
The results are stored in TFIDF_Synonyms folder in results folder


NOTE: We have modified the document ID for certain documents like '765' to '0765' in cacm.rel, because it would otherwise fetch the
wrong relevance data, kindly use the same file provided by us.

2) BM25:
python bm25.py <query-fileName> <output-folder> <index-filename>
1) To run BM25 on original query set:
python bm25.py originalQuery.txt BM25 index1gram.txt
The results are stored in BM25 folder in results folder

2) To run BM25 on originalQueryExpandedWithDerivatives.txt 
python bm25.py originalQueryExpandedWithDerivatives.txt BM25_Derivatives index1gram.txt
The results are stored in BM25_Derivatives folder in results folder

3) To run BM25 on originalQueryExpandedWithSynonyms.txt
python bm25.py originalQueryExpandedWithSynonyms.txt BM25_Synonyms index1gram.txt
The results are stored in BM25_Synonyms folder in results folder

3) LUCENE:

QUERY EXPANSION:

1.queryExpansion.py is the main file.
2.It imports FindCommonWords.py and QueryParsing.py. FindCommonWords.py takes common_words.txt(present in folder "files") as input.
3.QueryParsing.py takes cacm.query.txt as input
4.It generates expanded queries in pre-created queries folder.
5.inflectionalWords.txt and derivativeWords.txt are generated in a folder named "files" by running findSynonymsDerivatives.py.
6. queries_terms.txt is the file that is parsed to create inflectionalWords.txt and derivativeWords.txt files.

Steps :
1) Execute findSynonymsDerivatives.py to generate inflectionalWords.txt and derivativeWords.txt
python findSynonymsDerivatives.py
2) "queries" is the folder where output files are being created.
3) execute queryExpansion.py as 
python queryExpansion.py  
4) It generates all the expanded queries files in the queries folder.
Now we are ready with expanded queries. Task 1 can be re run taking on these expanded queries as inputs for tf-idf and BM25 rankings.

This gives us 5 files in total:

•	For Original queries:
	Path: /queries/originalQuery.txt
•	Queries expanded using derivatives
	Path: /queries/originalQueryExpandedWithDerivatives.txt
•	Queries expanded using synonyms 
	Path: /queries/originalQueryExpandedWithSynonyms.txt
•	Queries without stop/common words (Stopping)
	Path: /queries/queryWithoutStoppedWords.txt
•	Query expanded using derivatives without stop words 
	Path: /queries/stoppedQueryExpandedWithDerivatives.txt

	
STOPPING :
python tf-idf.py <query-fileName> <output-folder> <index-filename>

We perform stopping by running bm25 and tf-idf on queryWithoutStoppedWords.txt and
stoppedIndex.txt and store the results in Stop_BM25 and Stop_TFIDF folders respectively:

1)To run TFIDF on QueryWithoutStoppedWords.txt
python tf-idf.py QueryWithoutStoppedWords.txt Stop_TFIDF stoppedIndex.txt
The results are stored in Stop_TFIDF folder in results folder

2)To run BM25 on QueryWithoutStoppedWords.txt
python bm25.py QueryWithoutStoppedWords.txt Stop_BM25 stoppedIndex.txt
The results are stored in Stop_BM25 folder in results folder



STOPPING AND STEMMING:
python bm25.py <query-fileName> <output-folder> <index-filename>

We perform stopping and stemming by running bm25 and tf-idf on cacm_stem.query.txt and
stoppedStemmedIndex.txt and store the results in Stop_Stem_BM25 and Stop_Stem_TFIDF folders respectively.
NOTE: We have added the correct query numbers to the file cacm_stem.query.txt for correct reading and interpretation.
Kindly use the same file provided by us.

1)To run TFIDF on cacm_query.stem.txt
python tf-idf.py cacm_stem.query.txt Stop_Stem_TFIDF stoppedStemmedIndex.txt
The results are stored in Stop_Stem_TFIDF folder in results folder

2)To run BM25 on cacm_query.stem.txt
python bm25.py cacm_stem.query.txt Stop_Stem_BM25 stoppedStemmedIndex.txt
The results are stored in Stop_Stem_BM25 folder in results folder


EVALUATION:


The final runs obtained can be found in the results folder:

•	Lucene: Baseline run by the search engine with Lucene as the retrieval model 
•	BM25: Baseline run by the search engine with BM-25 as the retrieval model
•	BM25_Derivatives: Baseline run by the search engine with BM-25 as the retrieval model on the query set expanded by derivatives.
•	TFIDF_Derivatives: Baseline run by the search engine with TFIDF as the retrieval model on the query set expanded by derivatives.
•	TFIDF: Baseline run by the search engine with tf-idf as the retrieval model
•	BM25_Synonyms: Baseline run by the search engine with BM-25 as the retrieval model on the query set expanded by synonyms
•	TFIDF_Synonyms: Baseline run by the search engine with TFIDF as the retrieval model on the query set expanded by synonyms.
•	Stop_BM25: Baseline run by the search engine on queries without stopped words using BM25
•	Stop_TFIDF: Baseline run by the search engine on queries without stopped words using TFIDF
•	Stop_Stem_BM25: Baseline run by the search engine on stemmed queries without stopped words using BM25
•	Stop_Stem_TFIDF: Baseline run by the search engine on stemmed queries without stopped words using TFIDF

We perform evaluation by running:
python finalEvaluation.py 
on the first 9 results and store the _precisionAtK files and _Evaluation files (2 files for each run) 
in the evaluation folder. 



