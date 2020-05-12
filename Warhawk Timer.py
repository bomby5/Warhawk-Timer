from time import sleep
import winsound
time = input("How long would you like to set a timer for?(in minutes)")
sleep(int(time)*60)
print("time's up!")
frequency = 2500 # Set Frequency To 2500 Hertz
duration = 1000 # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
