import sys
import pygame
from pygame.locals import *
try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    import Mock.GPIO as GPIO
    
pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.display.set_mode((480, 320))
# sound = pygame.mixer.Sound('media/Boom Room 1 LR.wav')
sound = pygame.mixer.Sound('media/Bunker 6.0 test 1.wav')
playing = sound.play()
run=True
while run:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            run=False
  pygame.time.delay(100)
  if run==True:
    run = playing.get_busy()
  
sound.stop()
pygame.display.quit()
print("all done")
sys.exit()
