import html5lib,requests
from bs4 import BeautifulSoup as soup
import random
import pandas as pd

def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	return a
def write_this (path,data):
	f=open(path,'a+',errors='ignore')
	f.write(data)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText

def get_tags(data,tag):
	soups=soup(data,features="html5lib")
	TAGS=soups.findAll(tag)
	list1=[i for i in TAGS]
	return list1

def extractData(table):
	rows=table.findAll('tr')
	dataBox=[]
	c=0
	for i in rows:
		print(len(i))
		td=i.findAll('td',style=False) #NOTE : We have used the style selector because of inconsistency of data and structure of table.
		dataBox.append([x.text if x.text is not '' else '-' for x in td ]) #implicit method for aligning empty data with - symbol 
	return dataBox