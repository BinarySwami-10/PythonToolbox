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

def batch(times):
	for i in range(times):
		open_page(URL)
		time.sleep(random.random()/2)


URL='https://www.instagram.com'




# print(requests.get(URL).text)
reqNo=100


