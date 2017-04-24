import os
from os.path import isfile,join
from bs4 import BeautifulSoup
import re

list=os.listdir("htmls")
symbols=['"',"'",'@','#','$','~','`',':',';','^','*','_','?','%','(',')','{','}','[',']','+','=','<','>','|','\\','/']

def corpusGen():
    for file in list:
        if isfile (join("htmls",file)):
            with open('htmls/'+file, 'r') as content_file:
                content = content_file.read()
                content=content.decode('utf-8')
                soup= BeautifulSoup(content,"lxml")
                for script in soup.findAll('script',src=False):
                    script.decompose()
                text=soup.get_text()
                text=retainCommaDot(text)
                text=removeUrls(text)
                newText=''
                for char in text:
                    if ord(char) > 128 or char in symbols or ord(char) == 11 or ord(char)==9 or ord(char)==13:
                        char=''
                    elif ord(char) >= 65 and ord(char)<=91:
                        char=chr(ord(char)+32)
                    newText+=char
                
                newFileName=file.replace("html","txt")
                newFileName=newFileName.replace("_",'')
                writeFile=open('htmls/corpus/'+newFileName,"w")
                writeFile.write(newText)
                writeFile.flush()

def removeUrls(content):
    reUrl='http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls=re.findall(reUrl,content)
    for url in urls:
        #print url
        content=content.replace(url,'')
    return content

def retainCommaDot(content):
    punctList=[',','.']
    digits=['0','1','3','4','5','6','7','8','9']
    counter=0
    newStr=''
    for char in content:
        if char in punctList and  ( content[counter-1] not in digits or content[counter+1] not in digits) and counter != (len(content)-1):
                char=''
        newStr=newStr+char
        counter+=1

    return newStr
        
    
corpusGen()
        
                


