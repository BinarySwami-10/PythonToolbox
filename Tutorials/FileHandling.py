def write_this(name,String):
	f=open(name,"w+")
	f.write(String)

string='My name is nikhil'
write_this('testing.txt',string)