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
	TAGS=soups.findAll(tag,id='tdData')
	list1=[i for i in TAGS]
	return list1

#We found their api url via inspect element in browser and using this url
#as the content is javascript loaded beautiful soup was not able to get the rendered view of page
urlForAjaxRequests='https://www.bseindia.com/corporates/shpPublicShareholder.aspx?scripcd=532488&qtrid=105.00&QtrName=March%202020'
raw=open_page(urlForAjaxRequests)

tables=get_tags(raw,'div')
table=tables[0].table.findAll('tr')[4]
rows=table.findAll('tr')

# print(rows)

dataBox=[]

c=0
for i in rows:
	print(len(i))
	td=i.findAll('td',style=False) #We have used the style selector because of inconsistency of data and structure of table.
	dataBox.append([x.text if x.text is not '' else '-' for x in td ])

print(dataBox)
df = pd.DataFrame(dataBox[1:],columns=dataBox[0])
df.to_csv(r'BSE_Link2.csv',index=False)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)



