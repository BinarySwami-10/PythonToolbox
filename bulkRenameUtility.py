import os

dirlist=os.listdir()
os.chdir('ZeldaSongs')
currentDirectoryItems=os.listdir()

def replaceFunction():
	for item in currentDirectoryItems:
		newname=item.replace('.mp3.mp3','.mp3')
		os.rename(item,newname)
	print(os.listdir())

template='''  {
    type = "ambient-sound",
    name = "after-the-crash",
    track_type = "early-game",
    sound =
    {
      filename = "__base__/sound/ambient/after-the-crash.ogg"
    }
  },'''

subTemplate=template.split('\n')
print(subTemplate[-3])



# lps='\n'.join(spl)
# print(lps)