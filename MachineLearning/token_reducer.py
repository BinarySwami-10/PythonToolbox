from nltk import *
import json
def superStem(arr):
	global replacementDict
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
					# replacementDict[arr[i]].add(a)
					pass
			c+=1;# print(len(replacementDict[arr[i]]),end='|')
	print('Entities altered by stemming :',c)
	return arr

def dump_json(path,dicto):
	with open(path, 'w') as outfile:
	    json.dump(dicto, outfile,indent=4,sort_keys=True)
def load_json(path,dicto):
	with open(path, 'w') as infile:
	    dicto=json.load(infile)
	    return dicto
def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	print('File Opened And Engaged : ',path)
	return a
def write_this(path,content):
	f=open(path,"w+")
	f.write(content)


os.chdir('data\\bbc');

name='bbcData'
d={}
bigdata=[]
for j in range(1):
	fileitername=name+str(j)+'-t.txt'
	filebuff=read_this(fileitername)
	TextArr=filebuff.split()
	words = [word for word in TextArr if word.isalpha()]
	bigdata.extend(words) #open and extend file contents
	# write_this(name+str(j)+'-x.txt',' '.join(words))
	for i in words:
		try:
			d[i].append(i)
		except :
			d[i]=[]
			d[i].append(i)


wordHitDict=[(k,len(d[k])) for k,v in d.items()]
tuplist=sorted(wordHitDict,key = lambda x: x[1], reverse=True)
# print(tuplist)

commonWrdlist= [i[0] for i in tuplist][0:5000]
thinWordSet=set(commonWrdlist)
write_this('./bbctokens.txt'," ".join(commonWrdlist))

def Vocublary_Confiner(bigdata,vocublary):
	c=0;hit=0
	for i in bigdata:
		if i not in vocublary:
			bigdata[c]=''
			hit+=1
		c+=1
	print('entries removed %',round((hit/len(bigdata)*100),5))
	return bigdata

write_this('confined.txt',' '.join(Vocublary_Confiner(bigdata,thinWordSet)))


# #END HEAT MAP CALCULTOR BLOCK
# write_this(name+'HeatMap-t.txt'," ".join(bigdata)+str(hit))



# n_to_char = {n:char for n, char in enumerate(tokens)}
# char_to_n = {char:n for n, char in enumerate(tokens)}


# WHERE T suffix is truncated










# sentence='hello friends how are you doing my name is this and i love eating food and driving and go trump'.split()
# sentence=superStem(sentence)
# print(" ".join(sentence))
