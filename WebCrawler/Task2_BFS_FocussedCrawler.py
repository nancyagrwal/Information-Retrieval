import requests
from bs4 import BeautifulSoup
from time import sleep
import socket
import os
import sys
import time

def crawler(url, visited, keyword):
    print url
    # politeness policy of 1 sec between HTTP requests:
    time.sleep(1)
    source_txt = requests.get(url)

    plain_txt = source_txt.text.encode('utf-8')
    #implementing the beautiful soup library for parsing of data.
    soup = BeautifulSoup(plain_txt, "lxml")

    collection = []
    for txt in soup.findAll('a'):
        var = txt.get('href')
        tag_anchor = txt.text
        if var != None:
            if '.jpg' not in var and '.jpeg' not in var and  'Main_Page' not in var and '#' not in var and ':' not in var and 'JPG' not in var  :
                if var.find('/wiki/') is 0:
                    if 'solar' in var.lower() or 'solar' in tag_anchor.lower():
                        if '#' in var:
						    # # is used as an anchor to jump to an element with the same name/id
                            var.split('#')
                            var = var[0]
                        else:
                            var = var
                        a = 'https://en.wikipedia.org' + var
                        if a not in collection + visited:
                            # if the url is not in crawled and collection,append it to collection set.
                            collection.append(a)

    return collection

def get_url_for_5levels():
    count = 0
    #url = 'https://en.wikipedia.org/wiki/Sustainable_energy'
    seed_url = raw_input('enter seed URL : ')
    #keyword = 'solar'
    keyword = raw_input('enter keyword : ')
    url_to_process = [seed_url]
    crawled = list()
   
    while count < 5:
        print count
        processed = []
        for item in url_to_process:
            if item not in crawled:
                crawled.append(item)
                new_processed_list = crawled + url_to_process + processed
                processed += crawler(item , new_processed_list , keyword)
                url_to_process = processed
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

    file = open('Task2_BFS_FocussedCrawler.txt','w')
    for text in crawled:
        file.writelines(text+'\n')  # writing to the file



get_url_for_5levels()
