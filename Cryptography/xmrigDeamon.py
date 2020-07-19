import os
import sys
import time
import win32gui
import win32con
import win32api

try:
	import pyautogui
except :
	os.system('pip install pyautogui')

def getProgramID(ProgramName):
	#need to enter full program name
	hwndMain = win32gui.FindWindow(None,ProgramName)
	hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
	print(hwndMain,hwndChild)
	return hwndMain,hwndChild

def sendKey2Program(ID,key):
	# ID=String KEY=some_keyboard_key
	#Params: id, method, key, times
	temp = win32api.SendMessage(ID, win32con.WM_CHAR, ord(key), 1) 
	pass

def getObjectMethods(object):
	allMethods=dir(openWindows[0])
	methods= list (filter (lambda x:"__" not in x, allMethods))
	print(methods)

def pauseMiner(ID):
	sendKey2Program(ID,'p')

def playMiner(ID):
	sendKey2Program(ID,'r')

#Fuzzy search all Titles
windowNames=pyautogui.getWindowsWithTitle('xmrig 6') 

# get id of searched title by using internal method _hwnd 
ID=windowNames[0]._hWnd
print(ID)

while True:
	if pyautogui.getWindowsWithTitle('task'):
		print ('task O ba open',ID)
		pauseMiner(ID)
	else:
		playMiner(ID)
	time.sleep(1)



