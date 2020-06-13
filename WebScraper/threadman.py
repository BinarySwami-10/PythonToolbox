import time
import  threading
#import Thread as worker

threadBoard=[]
threadCount=10

for i in range(threadCount):
	threadBoard.append(threading.Thread(target=fun,args=(i,),name='ashul'+str(i) ))
	time.sleep(i/10)
	threadBoard[i].start()
	print('asasa')