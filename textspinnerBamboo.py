import html5lib,requests,random,pyautogui,time,clipboard
import threading
from bs4 import BeautifulSoup as soup

def spinbotForwarder(data):
	pyautogui.click(1390, 10)
	time.sleep(1)
	pyautogui.click(x=2172, y=665)
	pyautogui.click(x=2047, y=373)
	clipboard.copy(data)  
	pyautogui.hotkey('ctrl', 'v')

def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText
def get_p(Pagetext):
	soups=soup(Pagetext,features="html5lib")
	P=soups.findAll("p")
	pagecontent=[i.text for i in P]
	return " ".join(pagecontent)

def sentenceFlip(paragraph):
	trim=paragraph.split('\n')
	sentences=trim[0].split('.')
	for n in range(len(sentences)):
		sentences[n]=sentences[n].strip()
		try:
			if sentences[n][-1].isnumeric() or sentences[n+1][0].isnumeric() :
				sentences[n]+='.'+sentences[n+1]
				sentences[n+1]=''
		except :
			pass

	for n in range(2,len(sentences)-1,2):
		tmp=sentences[n]
		sentences[n]=sentences[n+1]
		sentences[n+1]=tmp
	return ' .'.join(sentences)

url='https://yoast.com/focus-on-long-tail-keywords/'

PageParagraph=get_p(open_page(url))
ArticleAlpha=sentenceFlip(PageParagraph)
time.sleep(2)

print(ArticleAlpha,pyautogui.position())
spinbotForwarder(ArticleAlpha)
