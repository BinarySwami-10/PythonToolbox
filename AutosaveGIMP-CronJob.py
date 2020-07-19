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
	hwndMain = win32gui.FindWindow(None,ProgramName)
	hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
	print(hwndMain,hwndChild)
	return hwndMain,hwndChild

def sendKey2Program(ID,key):
	#Params: id, method, key, times
	temp = win32api.SendMessage(ID, win32con.WM_CHAR, ord(key), 1) 
	pass

def getObjectMethods(object):
	allMethods=dir(openWindows[0])
	methods= list (filter (lambda x:"__" not in x, allMethods))
	print(methods)


theProgram=pyautogui.getWindowsWithTitle('GIMP' and 'layers')
title=list(map(lambda x: x.title, theProgram))[0]

theProgramID=getProgramID(title)
print(title)

sendKey2Program(theProgramID[0],'A')




