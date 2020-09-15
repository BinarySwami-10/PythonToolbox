import requests
import html5lib
from mxproxy import mx
from bs4 import  BeautifulSoup as soup


class Grammar:
	commonWords='the at there some my of be use her than and this an would first a have each make water to from which like been in or she him call is one do into who you had how time oil that by their has its it word if look now he but will two find was not up more long for what other write down on all about go day are were out see did as we many number get with when then no come his your them way made they can these could may I said so people part'.split()


class Stats:
	def __init__(self , text):  
		self.text  = text
		self.words = text.split()
		self.wordCount = len(self.words)

	def keywords(self):
		return set(words) - set(grammar.commonWords)

class Page:
	headers = {'User-Agent': 'Mozilla'}
	"""docstring for page"""
	def __init__(self, url):
		self.url 		=url
		self.rawpage 	=self.raw_page(self.url)
		self.soup 		=soup(self.rawpage,features="html5lib")
		self.text 		=self.plain_text(self.url)
		self.stats 		=Stats(self.text)

	def plain_text(self,url):
		return self.soup.text

	def raw_page(self,url):
		return requests.get(url,headers=self.headers).text

	def getTagContent(self,tag): 
	#tag or selector supported by beautiful soup
		return "".join( [x.text for x in self.soup.findAll(tag)] )

if __name__ == '__main__':
	url="https://www.investopedia.com/terms/c/credit.asp"
	page=Page(url)

	count=page.stats.wordCount
	print(count,)
	mx.jdump({"test":100,"rest":10},"test.json")
