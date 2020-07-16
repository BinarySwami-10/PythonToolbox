import pyautogui,time
import random
import threading
import tkinter as tk

def GetCursorCords():
	locX,locY=pyautogui.position()
	print ('({},{})'.format(locX,locY))

def keyboardPressThis(string):
	text=string
	print('Engaging')
	time.sleep(3)
	for i in text:
		pyautogui.typewrite(i,interval=random.random()/4)
def clickHere(cordinatesTuple):
	pyautogui.moveTo(cordinatesTuple)
	pyautogui.click()
def automatClick(clickSequence):
	# global itercount
	for t in range(itercount):
		for i,v in enumerate(clickSequence):
			clickHere(clickSequence[i])
			time.sleep(0.1)

itercount=1


colonizerfleet=[(1684,98),(2018,398),(2104,515),(1548,419),(1411,466),(1663,335)]
addToBuildQueue=[(1824,262),(1824,262),(2239,680)]
mergeAllFleet=[]




root = tk.Tk()
tk.ttk.Label(root,
	text = 'Stars Command Panel',
	font =('Verdana', 15)).pack(side = tk.TOP,
	pady = 10) 

frame = tk.Frame(root)
frame.pack()

Command1 = tk.Button(
	frame,text="Fleet Colonize cmd",
	command=lambda: automatClick(colonizerfleet))
Command1.pack(side=tk.LEFT)

Command2 = tk.Button(
	frame,text="iterAllPlanetQueues",
	command=lambda: automatClick(addToBuildQueue))
Command2.pack(side=tk.LEFT)

GetCursorCords = tk.Button(
	frame,text="GetCursorCords",
	command=GetCursorCords)
GetCursorCords.pack(side=tk.LEFT)

quit = tk.Button(frame,text="QUIT",fg="red",command=quit)
quit.pack(side=tk.LEFT)

root.mainloop()


