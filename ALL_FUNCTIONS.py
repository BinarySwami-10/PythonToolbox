def newest(path):
	#gets the newest FILE
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def exceptionHelper(err):
	if 'module' in str(err):
		prompts='you need to type this in cmd(windows)\n    '
		print(prompts,f'pip install  {str(err).split()[-1]}')
	pass


def write_this(fname,content):
	# SHORTHAND WRITE
	f=open(fname,"+ab")
	f.write(content)

def open_page(url):
	import sys
	try:
		import django
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
		fullText=requests.get(url,headers=headers).text
		return fullText
	except Exception as e:
		exceptionHelper(e)
		temp=e.__cause__.__sizeof__()
		print(sys._getframe(),dir(temp),temp)
		pass


print(open_page('https://www.tutorialspoint.com/rename-multiple-files-using-python'),"<--FROM PRINT()")
# import sys
# modules=list(sys.modules.keys())
# modules.sort()


