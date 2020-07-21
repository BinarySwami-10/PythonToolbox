import requests
import html5lib 
from bs4 import BeautifulSoup as soup

def get_page(url):
	response=requests.get(url).text
	return response


url='https://www.w3schools.com/python/default.asp'
htmlRaw=get_page(url)
htmlSoup=soup( get_page(url), 'html5lib')


sidenav=htmlSoup.find(id='sidenav')
links=sidenav.find_all('a')




# for l in links:
# 	print (l.text)
# print(links)
