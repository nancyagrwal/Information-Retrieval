import requests
from bs4 import BeautifulSoup
from time import sleep
import socket
import time

def crawler(url, depth, keyword):

    # politeness policy of 1 sec between HTTP requests:
	time.sleep(1)
	source_txt = requests.get(url)
	plain_txt = source_txt.text.encode('utf-8')
	
	# implementing the beautiful soup library for parsing of data.
	soup = BeautifulSoup(plain_txt, 'lxml')

	if(depth is 0): # no documents
		  return
		
	crawled = []
	element = soup.findAll('a')  # for fetching all required elements of the web page
	if len(crawled_list) >= 1000:
	    # we stop as soon as the fetched count becomes 1000.
		return
	for l in element:
		crawled.append(l.get('href'))
	anchor_array = []
	for j in element:
		anchor_array.append(j.text)
	for name in element:
		for seed in xrange(len(crawled)):
			if crawled[seed] is not None:
				if '#' not in crawled[seed] and ':' not in crawled[seed] and 'Main_Page' not in crawled:
					if crawled[seed].find('/wiki/') is 0:
						anchor = anchor_array[seed]
						if 'solar' in anchor.lower() or 'solar' in crawled[seed].lower():
						    # fetching links where solar is in href or the anchor text.
							if '#' in crawled[seed]:
							    # # is used as an anchor to jump to an element with the same name/id
								crawled[seed].split('#')
								crawled[seed] = crawled[seed][0]
							else:
								crawled[seed] = crawled[seed]
							temp_url = 'https://en.wikipedia.org' + crawled[seed]
							if(temp_url not in crawled_list):
								crawled_list.append(temp_url)
								print '\nURL Crawled: %s' %temp_url
								# recursing for links on lesser depth
								crawler(temp_url , depth-1 , keyword)  # recusrion
								
def dfs():
    
	seed_url = raw_input('enter seed URL : ')
	url = 'https://en.wikipedia.org/wiki/Sustainable_energy'
	#keyword = 'solar'
	keyword = raw_input('enter keyword : ')
	count = 0
	global crawled_list 
	crawled_list = list()
	depth = 5
	crawler(seed_url , depth, keyword)
	
	print len(crawled_list)
	crawled_list.append(url)
	crawled_list.pop(0)

	crawled_count = 1
	for d in crawled_list:
		time.sleep(1)  # politeness policy of 1 sec
		pg = requests.get(d)
		txt = pg.text.encode('utf-8')
		#scanner
		s = open("HTMLFile%s.txt" %crawled_count, "w") 
		s.write(txt)
		crawled_count+=1
		s.close
		
	file = open('Task2_DFS_FocussedCrawler.txt','w')
	for text in crawled_list:
		file.writelines(text+'\n')   # writing to the file


dfs()