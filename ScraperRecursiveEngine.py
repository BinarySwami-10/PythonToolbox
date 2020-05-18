import html5lib,requests,random
import threading
from bs4 import BeautifulSoup as soup

def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	return a
def write_this (path,data):
	f=open(path,'a+',errors='ignore')
	f.write(data)

def get_links(markup):
	unqlinks=[]
	soups=soup(markup,features="html5lib")
	post_links=soups.findAll("a",href=True)
	for i in post_links:
		url=i['href']
		if ('huff' in url and '' in url): #LOOKYOO
			unqlinks.append(url)
	unqlinks = list(set(unqlinks))
	return unqlinks

def get_p(Pagetext):
	soups=soup(Pagetext,features="html5lib")
	P=soups.findAll("p")
	pagecontent=[i.text for i in P]
	return " ".join(pagecontent)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	print("Just Visited : ", url)
	update_visited(url)
	return fullText

def update_visited(link):
	visited.add(link)
	write_this('visited.txt'," "+link)

def update_found(link_list):
	for link in link_list:
		found.add(link)
	write_this('found.txt'," "+link)

def allowedToVisit(i,inp):
	flag=0
	for x in inp:
		if i == x :
			flag=1
		else:
			pass
	return flag

def filterAllowedList(list_input):
	filtered=[]
	for i in onlyVisit:
		for j in list_input:
			if i in j:
				filtered.append(j)

	return filtered

found=set( read_this('found.txt').split() )
visited=set( read_this('visited.txt').split() )

print("-> visited Dictonary Length :: {}\n-> Pending Urls :: {}".format(visited.__len__(),found.__len__()) )
# REMOVE REPETITIONS # REMOVE REPETITIONS

onlyVisit=['www.huffpost.com'];
linkBuffer=list(found-visited);

for i in linkBuffer:
	if allowedToVisit(i.split('/')[2],onlyVisit)=='0' :
		print('exception ')
		linkBuffer.remove(i)
	else:
		try:
			currentPage=open_page(i) #as well as update visited
		except :
			pass
		write_this('huffpostData.txt', get_p(currentPage)+'\n\n' )

		lHolder=filterAllowedList( get_links(currentPage) ) #filter the list accord Condition
		update_found(lHolder)  #set Found's Update
		linkBuffer=list(found-visited);





