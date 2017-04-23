import requests
from bs4 import BeautifulSoup
from time import sleep
import socket
import os
import sys
import time


def crawler(url, crawled):
    
	# politeness policy of 1 sec between HTTP requests:
    time.sleep(1)
    source_txt = requests.get(url)
    plain_txt = source_txt.text.encode('utf-8')
	
	# implementing the beautiful soup library for parsing of data.
    soup = BeautifulSoup(plain_txt, "lxml")

    collection = []
    for txt in soup.findAll('a'):   # finding all the elements on the page
			var = txt.get('href')
			if var is not None:
				# we do not need images and colon and main page
				if '.jpg' not in var and 'JPG' not in var and '.jpeg' not in var  and 'Main_Page' not in var and ':' not in var :
					if var.find('/wiki/') is 0:
						if '#' in var:
						    # # is used as an anchor to jump to an element with the same name/id
							var = var.split('#')
							var = var[0]
						else:
							var = var
						a = 'https://en.wikipedia.org' + var
						if a not in collection + crawled:
						# if the url is not in crawled and collection,append it to collection set.
								collection.append(a)

    return collection

def get_url_for_5levels():
    count = 0
    seed_url = 'https://en.wikipedia.org/wiki/Sustainable_energy'
    url_to_process= [seed_url]
    crawled = list()
	
    while count < 5:
			print count
			processed_list = []
			for item in url_to_process:
				if item not in crawled:
					crawled.append(item)
					# the new list for crawling is the collection of already crawled and processed url's
					new_crawled_list = crawled + processed_list + url_to_process
					processed_list += crawler(item , new_crawled_list)
					
					url_to_process = processed_list
				if len(crawled) >= 1000:
					# do not crawl for more than 1000 urls
					break
			if len(crawled) >= 1000:
					# do not crawl for more than 1000 urls
					break
			count += 1

    crawled_count = 1
    for d in crawled:
	    # politeness policy of 1 sec
        time.sleep(1)
        pg = requests.get(d)
        txt = pg.text.encode('utf-8')
		#scanner
        s = open("HTMLFile%s.txt" %crawled_count, "w")
        s.write(txt)  
        crawled_count+=1
        s.close
    print len(crawled)

    file = open('Task1.txt','w')
    for text in crawled:
    	file.writelines(text+'\n')    # writing to the file



get_url_for_5levels()
