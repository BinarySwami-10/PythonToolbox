from mxproxy import mx
import hashlib
import requests

def get_image_links(url,selector):
	images=[]
	for x in mx.get_page_soup(url).select(selector):
		try:
			images.append(x['src'])
		except :
			images.append(x['data-src'])
	return images

def write_images(urllist):
	for x in urllist:
		x=x.split('?')[0]
		name=hashlib.md5(x.encode()).hexdigest()
		data=requests.get(x).content
		open(f'./images/{name}.png','wb').write(data)

def save_images_from_url(url):
	write_images(get_image_links(url,'picture img'))




if __name__ == '__main__':
	# url='https://www.goodhousekeeping.com/life/relationships/g25561929/broken-heart-quotes/?slide=1'


