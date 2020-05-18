from bs4 import  BeautifulSoup as soup
import glob
import lxml

#                            CODE Description
#Scans a directory content and creat a big file which is sum of all content

def write_this(fname,content):
	f=open(fname,"+ab")
	f.write(content)
def read_this (path):
	f=open(path,'rb+',).read()
	return f
def bs_all_content_of(tag):
	content=pageObject.findAll(tag)
	fullcontent=''
	for i in content:
		fullcontent += i.text
	return fullcontent
def join_strings(array):
	return ''.join(array)
def get_directory_files(dire):
	filelist=[]
	for file in glob.glob(dire):
	    filelist.append(file)
	return filelist
# filelist=get_directory_files("data\\blogs\\*")
# c=0
# gigaStringArray=[]
# for i in filelist:
# 	c+=1
# 	gigaStringArray.append(read_this(i))
# 	print ('status:' , c / len(filelist))
# c=0
# for i in gigaStringArray:
# 	c+=1
# 	write_this('VeryBigBlogArchive.txt',i)





