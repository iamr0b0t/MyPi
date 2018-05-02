# this program is to test LED On and OFF command from Adafruit API


import RPi.GPIO as GPIO
import time

from Adafruit_IO import Client
aio = Client('Here goes adafruit key')	# replace the string with your accounts key from adafruit.io
count = aio.receive('LEDBlink')         # LEDBlink is the feed name created on adafruit > https://io.adafruit.com

red = 7																	# assign pin value
yellow= 11
ourdelay = 1
GPIO.setwarnings(False)

## GPIO configuration
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

########################################
temp = count.value
print(count.value)


print("Total Blinks :"+ temp)

while 1:
	count = aio.receive('LEDBlink')
	if count.value == 'ON':
		GPIO.output(red, GPIO.HIGH)
		#time.sleep(0.5)
		GPIO.output(yellow,GPIO.HIGH)
		time.sleep(1)
	else:
		GPIO.output(red, GPIO.LOW)
		GPIO.output(yellow, GPIO.LOW)
		time.sleep(1)

GPIO.output(yellow, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(yellow, GPIO.LOW)
GPIO.cleanup()
