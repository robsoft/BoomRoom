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
pygame.font.init()
pygame.display.set_caption("BoomRoom")

size = [320, 480]
screen = pygame.display.set_mode(size)
# sound = pygame.mixer.Sound('media/Boom Room 1 LR.wav')
sound = pygame.mixer.Sound('media/Bunker 6.0 test 1.wav')
white = (255,255,255)
grey =  (169,169,169)
black = (  0,  0,  0)
red = (255,0,0)
green = (0,255,0)
redbutton = pygame.Rect((10,10),(300,200))
greenbutton = pygame.Rect((10,220),(300,200))
pygame.draw.rect(screen, red, redbutton)
pygame.draw.rect(screen, green, greenbutton)

FPS = 60
FramePerSec = pygame.time.Clock()

pygame.display.flip()

playing = sound.play()
run=True
while run:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
            run=False
            break
  
  pygame.display.update()
  FramePerSec.tick(FPS)      
  # pygame.time.delay(100)
  if run==True:
    run = playing.get_busy()
  
sound.stop()
pygame.display.quit()
pygame.quit()
print("all done")
sys.exit(0)
