import os
from bs4 import BeautifulSoup
import socket
import sys
import requests

docIdList=[]
urlList=[]
graph={'':[]}

def generateDocIds(): 
        with open("Task1.txt","r") as f:
           for line in f:
                
                urlList.append(line.replace('\n',''))
                lineArray=line.split('/')
                docIdList.append(lineArray[len(lineArray)-1].replace('\n',''))
        #print urlList
                
        #print docIdList
        for line in docIdList:
                url='https://en.wikipedia.org/wiki/' + line
                #print url
                #source_txt=(urllib.request.urlopen(urlObj.url)).read()
                source_txt = requests.get(url)
                plain_txt = source_txt.text.encode('utf-8')
                soup = BeautifulSoup(plain_txt, "lxml")
                for txt in soup.findAll('a'): # finding all the elements on the page
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
                                                #print var
                                                a = 'https://en.wikipedia.org' + var
                                                #print a
                                                if a in urlList:
                                                        docArr=a.split('/')
                                                        docId=docArr[len(docArr)-1].replace('\n','')
                                                        #print docId
                                                        if graph.has_key(docId):
                                                                listD=graph[docId]
                                                                if line not in listD:
                                                                        listD.append(line)
                                                                        graph[docId]=listD
                                                        else:
                                                                listD=[]
                                                                listD.append(line)
                                                                graph[docId]=listD
                                                        #print graph
        
        return graph
def main():
        docGraph=generateDocIds()
        fileWrite=open("G1.txt","w")
        keys=docGraph.keys()
        for key in keys:
                inlinks=docGraph.get(key)
                fileWrite.write(key+'')
                for docs in inlinks:
                        fileWrite.write(docs+' ')
                fileWrite.write('\n')
				
        #fileWrite.flush()
main()
