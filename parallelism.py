import os, sys
import time,timeit
from multiprocessing import Pool,Process,Queue,Pipe

globala='someValue'


def f(x,conn):
	global globala
	globala+='+f'
	print(globala + ' from f')
	conn.send(globala + ' f Piped this')
	
if __name__ == '__main__':
	m_conn,child_conn = Pipe()
	p1 = Process(target=f, args=(50,child_conn,))
	p1.start()
	p1.join()
	# m_conn,child_conn = Pipe()
	# p2 = Process(target=f, args=(50,child_conn,))
	# p2.start()
	# p2.join()
	print (m_conn.recv(), globala)  



