
import sys
success=0
importlevel=""

for i in range(4):
	if not success:
		try:
			sys.path.append(importlevel)
			from modulex import modulex as mx
			print("mx imported")
			success=1
			mx.cleanup()
		except Exception as e:
			# print(e)
			importlevel=importlevel + "../"
	else:
		pass

		





