def read_this (path):
	a=''
	f=open(path,'r',errors='ignore')
	a+=f.read()
	return a

def write_this(fname,content):
	f=open(fname,"w+")
	f.write(content)

arr=list(set(read_this('found.txt').split('\n')))
write_this('found1.txt','\n'.join(arr))
