import pyautogui,time
import html5lib,requests,random
import threading
from bs4 import BeautifulSoup as soup
from pyautogui import typewrite
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
	typewrite(string,interval=0.0001)

def clickHere(cordinatesTuple):
	pyautogui.moveTo(cordinatesTuple)
	pyautogui.click()

def macroClick():
	for i,v in enumerate(clickSequence[:6]):
		clickHere(clickSequence[i])
		time.sleep(0.15)


# clickSequence=[(1684,98),(2018,398),(2104,515),(1548,419),(1411,466),(1663,335)]
string='''{
    "api": {
        "id": null,
        "worker-id": null,
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": true,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": ["0x1a4:0x7"],
        "numa": false
    },
'''
keyboardPressThis(string)

