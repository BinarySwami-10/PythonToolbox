import html5lib,requests
import threading
from bs4 import BeautifulSoup as soup
import random

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
	update_visited(url)
	fullText=requests.get(url,headers=headers).text
	print(threading.current_thread().getName(), " Just Visited : ", url)
	return fullText

def update_visited(link):
	visited.add(link)
	write_this('visited.txt',"\n"+link)

def update_found(link_list):
	for link in link_list:
		found.add(link)
		write_this('found.txt',"\n"+link)

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
			try:
				if i in j.split('/')[2]:
					filtered.append(j)
			except :
				# print('bug during filter :: PAssed')
				pass

	return filtered

#checkpoint Preloading
found=set( read_this('found.txt').split('\n') )
visited=set( read_this('visited.txt').split('\n') )

print("-> visited Dictonary Length :: {}\n-> Pending Urls :: {}" \
	.format(visited.__len__(),found.__len__()) )
# REMOVE REPETITIONS # REMOVE REPETITIONS
linkBuffer=list(found-visited)
onlyVisit=['www.huffpost.com','www.huffingtonpost.in']

def explorer():
	global linkBuffer,onlyVisit
	global found,visited
	linkBuffer=list(found-visited)	
	for i in linkBuffer:

		try:
			currentPage=open_page(random.choice(linkBuffer)) #as well as update visited
		except Exception as s:
			print(s)
			pass
		write_this('huffpostData.txt', get_p(currentPage)+'\n\n' )
		lHolder=filterAllowedList( get_links(currentPage) ) #filter the list accord Condition
		# print(lHolder)
		update_found(lHolder)  #set Found's Update
		linkBuffer=list(found-visited)	
pass

def visitor(index):
	global linkBuffer
	global found,visited
	linkBuffer=list(found-visited)	
	for i in linkBuffer:
		# visited=set( read_this('visited.txt').split('\n') )
		try:
			currentPage=open_page(random.choice(linkBuffer)) #as well as update visited
			# print('Thread-',i,'vi')
			write_this('huffpostData.txt', get_p(currentPage)+'\n\n' )
		except :
			print('page skipped')
			pass
		linkBuffer=list(found-visited)	

	pass

# explor1=threading.Thread(target=explorer,)
# explor1.start()
# explor2=threading.Thread(target=explorer,)
# explor2.start()
# explor3=threading.Thread(target=explorer,)
# explor3.start()
# explor4=threading.Thread(target=explorer,)
# explor4.start()


threadBoard=[]
threadCount=25

for i in range(threadCount):
	threadBoard.append(threading.Thread(target=visitor,args=(i,) ))
	threadBoard[i].start()
	print('Thread-',i,' HasBeenStarted')




