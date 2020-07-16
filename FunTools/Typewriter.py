import pyautogui,time
import html5lib,requests,random
import threading
from bs4 import BeautifulSoup as soup
def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText
def get_span(Pagetext):
	soups=soup(Pagetext,features="html5lib")
	P=soups.findAll("span",class_='wblack')
	pagecontent=[i.text for i in P]
	return "".join(pagecontent)

def keyboardPressThis(string):
	text=string
	print('Engaging')
	time.sleep(3)
	for i in text:
		pyautogui.typewrite(i,interval=random.random()/4)

def clickHere(cordinatesTuple):
	pyautogui.moveTo(cordinatesTuple)
	pyautogui.click()

def macroClick():
	for i,v in enumerate(clickSequence[:6]):
		clickHere(clickSequence[i])
		time.sleep(0.15)


clickSequence=[(1684,98),(2018,398),(2104,515),(1548,419),(1411,466),(1663,335)]



 # pyautogui.position()

