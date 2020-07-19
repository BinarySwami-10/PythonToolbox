import winsound
import time

for i in range(100):
	frequency = 500  # Set Frequency To 2500 Hertz
	duration = 1000  # Set Duration To 1000 ms == 1 second
	winsound.Beep(frequency, duration)
	time.sleep(1)