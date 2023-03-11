# BoomRoom
# v1.01
# 
# for Hack Green 'Secret Nuclear Bunker'
#
# initial dev version
#
# designed for a 320x480 resistive-touch screen
#
# media in a subfolder 'media'
# when running,
#  key 'T' will start a test (if not currently active)
#  key 'R' will start a run (if not currently active)
#  key 'S' will stop whatever is currently active
#  any other key will end the program (for now)
#  likewise, buttons can be pressed on screen with the mouse/stylus etc
#


import sys
import pygame
from pygame.locals import *

try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    import Mock.GPIO as GPIO


def centreImgOut(screen, img, xbound, ybound, xofs, yofs):
    ofs=img.get_rect()
    screen.blit(img, ( xofs + ((xbound-ofs.width)/2), yofs + ((ybound-ofs.height)/2)) )
  
def setup():
    global clrWhite, clrGrey, clrWhite, clrBlack, clrRed, clrAmber, clrGreen
    global screen, font
    global fps, clock
    global rectTop, rectBottom
    global imgTest, imgRun, imgTestStop, imgRunStop, imgLogo
    global isActive
    global sound, soundChannel
  
    print("Starting up")
    pygame.init()
    pygame.mixer.init()
    pygame.display.init()
    pygame.font.init()
    pygame.mouse.set_visible(True)
    pygame.display.set_caption("BoomRoom")
    clrWhite = (255,255,255)
    clrGrey =  (169,169,169)
    clrBlack = (0,0,0)
    clrRed = (255,0,0)
    clrGreen = (0,255,0)

    font = pygame.font.SysFont(None, 132)
    lsize = [320, 480]
    screen = pygame.display.set_mode(lsize)
    lsizeButton = (300,220)
    rectTop = pygame.Rect((10,10),lsizeButton)
    rectBottom = pygame.Rect((10,250),lsizeButton)
    imgTest = font.render('Test', True, clrBlack)
    imgTestStop = font.render('Stop', True, clrBlack)
    imgRun = font.render('Run', True, clrWhite)
    imgRunStop = font.render('Stop', True, clrWhite)
    imgLogo = pygame.image.load('media/Bunker_220x220.png')

    fps = 30
    clock = pygame.time.Clock()

    # need to have something initialised in 'sound'?
    sound = pygame.mixer.Sound('media/Boom Room 1 LR.wav')

def shutdown():
    print("shutting down")
    sound.stop()
    pygame.mouse.set_visible(True)
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)

def doReset():
    global sound, soundChannel
    global isActive
    pygame.event.clear()
    sound.stop()
    # setup the buttons again
    setButton(rectTop, clrGreen, imgTest)
    setButton(rectBottom, clrRed, imgRun)
    pygame.display.flip()
    pygame.event.clear()
    isActive=False
  
def doRun():
    print("running")
    global sound, soundChannel
    global isActive
    sound.stop()
    setButton(rectTop, clrBlack, imgLogo)
    setButton(rectBottom, clrRed, imgRunStop)
    pygame.display.flip()
    sound = pygame.mixer.Sound('media/Boom Room 1 LR.wav')
    pygame.event.clear()
    soundChannel = sound.play()
    isActive=True
    pygame.event.clear()
  

def doTest():
    print("testing")
    global sound, soundChannel
    global isActive
    sound.stop()
    setButton(rectTop, clrGreen, imgTestStop)
    setButton(rectBottom, clrBlack, imgLogo)
    pygame.display.flip()
    sound = pygame.mixer.Sound('media/Bunker 6.0 test 1.wav')
    pygame.event.clear()
    soundChannel=sound.play()
    isActive=True
    pygame.event.clear()

def topButtonPressed():
    global isActive
    if isActive==True:
      doReset()
    else:
      doTest()
    
def bottomButtonPressed():
    global isActive
    if isActive==True:
      doReset()
    else:
      doRun()

def setButton(buttonRect, color, img):
    pygame.draw.rect(screen, color, buttonRect)
    centreImgOut(screen, img, buttonRect.width, buttonRect.height, buttonRect.left, buttonRect.top)



# Main Program

setup()
doReset()

  
running=True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running=False
            break
    
        if event.type == pygame.MOUSEBUTTONUP:
            mousepos=pygame.mouse.get_pos()
            if rectTop.collidepoint(mousepos):
                topButtonPressed()
                break
    
            if rectBottom.collidepoint(mousepos):
                bottomButtonPressed()
                break
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                doReset()
                break

            if event.key == pygame.K_t:
                topButtonPressed()
                break
            if event.key == pygame.K_r:
                bottomButtonPressed()
                break
            # otherwise just baIl anyway
            running=False
            break
        
    # end for event loop

    # are we still actively doing something?
    if running and isActive:
        # have we come to the end of the active sound?
        if soundChannel.get_busy() == False:
            doReset()
      
    # finish off housekeeping etc      
    pygame.display.update()
    clock.tick(fps)
    
# end while run


# we have stopped running, it's time to shutdown    
print("stopped running")

shutdown()  
