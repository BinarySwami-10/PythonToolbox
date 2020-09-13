import html5lib,requests,time,threading,selenium
from selenium import webdriver
from bs4 import BeautifulSoup as soup

def imgDownload(url,name):
	img_data = requests.get(url).content
	with open(str(name)+'.jpg', 'wb') as handler:
	    handler.write(img_data)
	print('downloaded :'+url)

def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)

def open_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	fullText=requests.get(url,headers=headers).text
	return fullText

def get_imgs(Pagetext):
	arr=page.split("'")
	url=[x for x in arr if ('png' in x) or ('jpg' in x) and ('http' in x) ]
	# soups=soup(Pagetext,features="html5lib")
	return url

wd = webdriver.Firefox()
page=wd.get('https://pixabay.com/images/search/nature/')
# print(page)

urlWheel=get_imgs(page)



def hire_employer(work,workdata,employee_count):
	workbench=[]
	workslots=[workdata[i:i + employee_count] for i in range(0, len(workdata), employee_count)]

	namer=0
	for slot in workslots:
		for j in slot:
			workbench.append( threading.Thread( target=work, args=(j,namer) ) )
			try:
				workbench[namer].start()
				workbench[namer].join()
				namer+=1
			except:
				print('error occured')

		time.sleep(0.5)


# hire_employer(imgDownload,urlWheel,4)