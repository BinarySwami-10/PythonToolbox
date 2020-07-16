from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import html5lib,requests,random,pyautogui,time,clipboard
import threading
from bs4 import BeautifulSoup as soup

def open_page(url):
	global totreq
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	totreq+=1
	print(totreq)
	# return fullText

def open_page_with_selenium(url):
	wd.get(url)
	markup= wd.page_source
	return markup



opts=webdriver.firefox.options.Options()
# opts.headless = True 
# opts.add_argument("--headless") #works standalone
client = webdriver.Firefox(options=opts)


URL='https://www.instagram.com'
client.get(URL)



