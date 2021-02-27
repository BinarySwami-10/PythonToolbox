from mxproxy import mx
import hashlib
import requests
import os
from PIL import Image

SAVE_FOLDER_NAME='sabji_images/'

def data_splitter(dataList,pieces):
	dataparts=[]
	for d in range(pieces):
		step=int(len(dataList)/pieces)+1
		subdata=dataList[d*step:(d+1)*step]
		dataparts.append(subdata)
	return dataparts

def multi_thread(workfn,work,parallelism=4):
	import threading
	threadpool=[threading.Thread(target=workfn,args=(work[x],)) for x in range(parallelism)]
	return threadpool

def get_image_links(url,selector):
	images=[]
	for x in mx.get_page_soup(url).select(selector):
		try:
			images.append(x['src'])
		except :
			images.append(x['data-src'])
	return images

def write_images(urllist,dirname=SAVE_FOLDER_NAME):
	mx.touch(dirname+'init.txt')
	for x in urllist:
		# x=x.split('?')[0]
		filename=hashlib.md5(x.encode()).hexdigest()
		writepath=f'./{dirname}{filename}'
		if not os.path.exists(writepath):
			print('downloading=>',x)
			data=requests.get(x).content
			try:
				open(writepath,'wb').write(data)
				print('writing=>',x,writepath)
			except Exception as e:
				print('failed',x)

def save_images_from_url(url):
	write_images(SAVE_FOLDER_NAME,get_image_links(url,'picture img'))



def yandex_image_gatherer(markup):
	resultPageSoup=mx.make_soup(markup)
	results=resultPageSoup.select('.serp-item[data-bem]')
	urls=[mx.jloads(x['data-bem'])['serp-item']['img_href'] for x in results]
	return urls

if __name__ == '__main__':
	url='https://yandex.com/images/search?text=nature'
	markup=mx.fread('./rawData/yashresults1.html')
	urls=yandex_image_gatherer(markup)
	work=data_splitter(urls,4)
	threadpool=multi_thread(write_images,work)
	[x.start() for x in threadpool];
	[x.join() for x in threadpool];

	# write_images(SAVE_FOLDER_NAME,urls)



	def identify_format_and_rename(dirname):
		for x in os.listdir(dirname):
			x=dirname+x
			try:
				iformat=Image.open(x).format
				os.rename(x,f'{x}.{iformat}')
				
			except Exception as e:
				print('rename error for', x,e)

	identify_format_and_rename(SAVE_FOLDER_NAME)
