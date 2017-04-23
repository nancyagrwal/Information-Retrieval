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
    for txt in soup.findAll('a'):
    	name = txt.get('href')
        if name is not None:
            if '.jpg' not in name and '.jpeg' not in name  and 'Main_Page' not in name and 'JPG' not in name and ':' not in name :
                if name.find('/wiki/') is 0:
                    if '#' in name:
					    # # is used as an anchor to jump to an element with the same name/id
                        newvar = name.split('#')
                        newvar = newvar[0]
                    else:
                        newvar = name
                    a = 'https://en.wikipedia.org' + newvar
                    if a not in collection + crawled:
					    # if the url is not in crawled and collection,append it to collection set.
                        collection.append(a)

    return collection

def get_url_for_5levels():

    count = 0
    url = 'https://en.wikipedia.org/wiki/Solar_power'
    url_to_process= [url]
    crawled = list()
    while count < 5:
        print count
        processed_list = []
        for item in url_to_process:
            if item not in crawled:
                	crawled.append(item)
				
                	processed_list += crawler(item, crawled + url_to_process + processed_list)
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
        time.sleep(1)
        pg = requests.get(d)
        txt = pg.text.encode('utf-8')
		#scanner
        s = open("HTMLFile%s.txt" %crawled_count, "w")
        s.write(txt)
        crawled_count+=1
        s.close
    print len(crawled)

    file = open('Task3.txt','w')
    for text in crawled:
    	file.writelines(text+'\n')  # writing to the file



get_url_for_5levels()
