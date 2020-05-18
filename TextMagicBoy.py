import string,re,os,json
from nltk import *
import multiprocessing
from multiprocessing import Process
# from nltk.corpus import names 

def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	print('File Opened And Engaged : ',path)
	return a
def write_this(path,content):
	f=open(path,"w+")
	f.write(content)
def write_json(path,dicto):
	with open(path, 'w') as outfile:
	    json.dump(dicto, outfile,indent=4,sort_keys=True)

def remove_numbers(text): 
    result = re.sub(r'\d+', '', text) 
    return result 
def remove_punctuation(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 
def master_clean(text):
	# result = re.sub( r' ' , '.' ,  text).lower()
	result=text.lower()
	translator = str.maketrans('1234567890-', '           ', '”“‘’\\/[]()'+string.punctuation)
	translator = str.maketrans('', '', '1234567890')
	result = result.translate( translator )
	# result = result.replace()
	return result

def superStem(name,j):
	print('asdas')
	fileitername=name+str(j)+'.txt'
	arr=read_this(fileitername).split()
	replacementDict={}
	c=0
	stem = SnowballStemmer('english')
	for i in range(len(arr)) :
		a=arr[i]
		arr[i]=stem.stem(arr[i])

		if a!=arr[i]:
			if arr[i] in replacementDict:
					replacementDict[arr[i]].append(a)
			else:
					replacementDict[arr[i]]=[a]
					pass
			c+=1;
	fwname=name+str(j)+'-t.txt'
	write_this(fwname, " ".join( arr ) )
	print('Entities altered by stemming :',c )
	write_json('bbcDataT'+str(j)+'.json',replacementDict)
	return arr

def dict_shrink(replacementDict):
	print('Removing Duplicates from ',replacementDict)
	for i in replacementDict: #REMOVE DUPLICATES
		unik=list(set(replacementDict[i]))
		replacementDict[i]=unik
	return replacementDict
	pass

def file_magick_open(contains):
	filelist=os.listdir()
	for i in range(len(filelist)):
		if contains in filelist[i]:
			filename=filelist[i];
			print('|i=',i,filelist[i])
	return filename

def make_blobs(path,pieces):
	arr=read_this(path).split()
	BlobNumbers=int(len(arr)/pieces)
	for i in range(pieces):
		block=arr[i*BlobNumbers : (i+1)*BlobNumbers]
		write_this(path.split('.')[0]+str(i)+'.txt', ' '.join(block))
	pass
# make_blobs(namecontains,5)
def polish_man(name,):
	for i in range(5):
		fileitername=name+str(i)+'.txt'
		filebuff=read_this(fileitername)#.replace("Subscribe to the BBC News Magazine's email newsletter to get articles sent to your inbox",'')#.replace(',',' , ').replace('.',' . ').replace(':',' ').replace('?',' ? ').replace('-',' - ').replace('(',' ( ').replace(')',' ) ')
		s=filebuff.lower()
		s = re.sub(r'( \' )', '\'', s)
		s = re.sub(r'(“|”)', '"', s)
		print(s[0:1000])
		# s=re.sub(r'','',filebuff)
		# s=re.sub(r'\S* sa(ys|id)','name said',filebuff)
		# s=re.sub(r'\'','\'',s)
		trunkname=fileitername[0:-4]+'-t.txt'
		write_this(trunkname,s)
	pass


name='bbcData'
procpool=[]
if __name__=="__main__":

	os.chdir('data');
	for i in range(1):
		procpool.append(Process(target=superStem,args=(name,4)))
		procpool[i].start()







