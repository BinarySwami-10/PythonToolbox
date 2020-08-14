from bs4 import BeautifulSoup as soup
import html5lib
def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)

html = open("PPE.html",'r', encoding="utf8").read()
soup = soup(html,features='html5lib',)

metatag = soup.new_tag('meta')
metatag.attrs['charset'] = 'utf-8'


soup.head.append(metatag)
print(soup)


