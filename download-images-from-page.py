import html5lib,requests,random,pyautogui,time,clipboard
import threading
from bs4 import BeautifulSoup as soup

def imgDownload(url,name):
	img_data = requests.get(url).content
	with open('quotes\\'+name, 'wb') as handler:
	    handler.write(img_data)

def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText

def get_img(Pagetext):
	soups=soup(Pagetext,features="html5lib")
	IMG=soups.findAll("img")
	imlist=[i.get('data-src') for i in IMG]
	return imlist

page=open_page('https://www.goodhousekeeping.com/health/wellness/g2401/inspirational-quotes/')
imgarray=get_img(page)
filtered=[str(x) for x in imgarray if True ]

c=0
for i in filtered:
	try:
		imgDownload(i,'inspirational-'+str(c)+'.png')
		c+=1
	except :
		print('FAILED : ',i)
print(filtered)

