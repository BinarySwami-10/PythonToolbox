import selenium,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

#OPENSOURCE CODE By NIKHIL SWAMI
def pushTab(url):
	driver.execute_script("window.open('{}', '_blank')".format(url))


def read_this(path):
	f=open(path,"+r",errors="ignore").read()
	return f

def getQuestionsFromClass(someClass):
	soups=soup(markup,features="lxml")
	List = soups.findAll("div",class_=someClass)
	pagecontent=[i.text for i in List if (len(i.text.split())>3)]
	return "\n".join(pagecontent)


#important : inspect the class on browser which contains questions and pass it here in below variable.
questionContainingClass='freebirdFormviewerViewItemsItemItemTitleContainer'

#important: Copy paste the html of page containing questions as it is. just copy the content of body tag
# and put in the page.html file so the code reads it and extract the questions from the class == questionContainingClass

markup=read_this('page.html') #this must come first before get questions function
QuestionQueryList=getQuestionsFromClass(questionContainingClass).split('\n')


googlize=list(map(lambda i:'https://www.google.com/search?q='+i.replace("'","") , QuestionQueryList))
print(googlize)

driver = webdriver.Firefox()
for i in googlize:
	time.sleep(1) #time interval for each result to load in new tab dont set to 0 as google will block you. :-P
	pushTab(i)

#OPENSOURCE CODE By NIKHIL SWAMI



