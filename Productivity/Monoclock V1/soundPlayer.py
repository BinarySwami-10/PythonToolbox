import winsound
import time
import os,sys
import json

conf='config.json'

def make_settings(obj,savepath):
	#dict 2 json
	fp=open(savepath,'+w')
	json.dump(obj,fp)
	#
# options={"interval":"10000","status":"1"}
# make_settings(options,'config.json')


def get_settings():
	fp=open(conf,'r')
	return json.load(fp)

def beeeep():
	frequency = 1000  # Set Frequency To 2500 Hertz
	duration = 400  # Set Duration To 1000 ms == 1 second
	winsound.Beep(frequency, duration)


options=get_settings()
while options["status"]:
	try:
		beeeep()
		time.sleep(options['interval'])
		options=get_settings()

	except Exception as e:
		print("audio loop != breaked",e)
		break
