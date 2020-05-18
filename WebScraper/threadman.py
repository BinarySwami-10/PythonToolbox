import time
import  threading
#import Thread as worker

v1,v2,v3,v4=1,2,3,4
def fun(t):
	global v1,v2,v3,v4
	v2=v2+v2
	print (threading.currentThread().getName()+ 'modified global as ' ,v2)

threadBoard=[]
threadCount=10

for i in range(threadCount):
	threadBoard.append(threading.Thread(target=fun,args=(i,),name='ashul'+str(i) ))
	time.sleep(i/10)
	threadBoard[i].start()
	print('asasa')