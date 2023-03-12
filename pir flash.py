

import RPi.GPIO as GPIO
import time

sensor = 36
led = 38, 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,True)
print ("Initialzing PIR")
time.sleep(5)
print ("PIR Ready")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(led,False)
          print ("Motion Detected")
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(led,True)


except KeyboardInterrupt:
    GPIO.cleanup()
