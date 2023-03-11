# BoomRoom
# v1.05
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
import socket

try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    import Mock.GPIO as GPIO

import BRRunMode as RunMode
import BRTestMode as TestMode

def get_ip_address():
   ip_address = 'n/a';
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8",80))
   ip_address = s.getsockname()[0]
   s.close()
   return ip_address

def centreImgOut(screen, img, xbound, ybound, xofs, yofs):
    ofs=img.get_rect()
    screen.blit(img, ( xofs + ((xbound-ofs.width)/2), yofs + ((ybound-ofs.height)/2)) )
  
def setup():
    global clrWhite, clrGrey, clrWhite, clrBlack, clrRed, clrAmber, clrGreen
    global screen, font
    global fps, clock
    global rectTop, rectBottom, rectIP
    global imgTest, imgRun, imgTestStop, imgRunStop, imgLogo, imgIP
    global isActive, activeStartTime
    global sound, soundChannel

    global eventList
    eventList = list(())
    global idxEventList
    idxEventList=0
    global hasEvents
    hasEvents=len(eventList)>0

    global modeFuncs
    
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

    lsize = [320, 480]
    screen = pygame.display.set_mode(lsize)

    font = pygame.font.SysFont(None, 32)
    imgIP = font.render(get_ip_address().replace('.',' . '), True, clrWhite)

    font = pygame.font.SysFont(None, 132)
    imgTest = font.render('Test', True, clrBlack)
    imgTestStop = font.render('Stop', True, clrBlack)
    imgRun = font.render('Run', True, clrWhite)
    imgRunStop = font.render('Stop', True, clrWhite)
    imgLogo = pygame.image.load('media/Bunker_200x200.png')

    lsizeButton = (300,200)
    rectTop = pygame.Rect((10,10),lsizeButton)
    rectBottom = pygame.Rect((10,230),lsizeButton)
    rectIP = pygame.Rect((10,450),(300,30))

    fps = 30
    clock = pygame.time.Clock()

    # TODO: need to have something initialised in 'sound'?
    sound = pygame.mixer.Sound('media/Boom Room 1 LR.wav')


def shutdown():
    print("shutting down")
    sound.stop()
    pygame.mouse.set_visible(True)
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)

def boomOne():
    print("boomOne hit")
    
def boomTwo():
    print("boomTwo hit")
    
def boomThree():
    print("boomThree hit")
    
def boomFour():
    print("boomFour hit")

def doReset():
    print("reset")
    global sound, soundChannel
    global isActive, activeStartTime
    global eventList
    sound.stop()
    eventList.clear()
    resetEventList()
    #modeFuncs.clear()
    
    # setup the buttons again
    setButton(rectTop, clrGreen, imgTest)
    setButton(rectBottom, clrRed, imgRun)
    setButton(rectIP, clrBlack, imgIP)
    pygame.display.flip()

    isActive=False
    activeStartTime = pygame.time.get_ticks()
    pygame.event.clear()


def doRun():
    print("running")
    global sound, soundChannel
    global isActive, activeStartTime
    global eventList
    sound.stop()
    RunMode.ModeInit(eventList)
    resetEventList()
    global modeFuncs
    modeFuncs = RunMode.ModeFuncs()

    setButton(rectTop, clrBlack, imgLogo)
    setButton(rectBottom, clrRed, imgRunStop)
    pygame.display.flip()

    sound = pygame.mixer.Sound(RunMode.GetSoundFile())
    soundChannel = sound.play()
    isActive=True
    activeStartTime = pygame.time.get_ticks()
    pygame.event.clear()


def doTest():
    print("testing")
    global sound, soundChannel
    global isActive, activeStartTime
    global eventList
    sound.stop()
    TestMode.ModeInit(eventList)
    resetEventList()
    global modeFuncs
    modeFuncs = TestMode.ModeFuncs()
    
    setButton(rectTop, clrGreen, imgTestStop)
    setButton(rectBottom, clrBlack, imgLogo)
    pygame.display.flip()

    sound = pygame.mixer.Sound(TestMode.GetSoundFile())
    soundChannel=sound.play()
    isActive=True
    activeStartTime = pygame.time.get_ticks()
    pygame.event.clear()
    
def resetEventList():  
    global hasEvents, idxEventList, eventList
    idxEventList=0
    hasEvents=len(eventList)>0  


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

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

# Main Program

setup()

print(get_ip_address())

# make a list of possible function calls the eventList could contain
boomFuncs = globals().copy()
boomFuncs.update(locals())

doReset()

running=True
while running:
    # is there anything to do right now?
    if isActive and hasEvents:
        elapsed = pygame.time.get_ticks()

        # when is the next event?
        eventTime = eventList[idxEventList][0]
        
        # is this event happening now (or has passed?)
        if (activeStartTime + eventTime <= elapsed):

            # find the eventList function call in our instance
            methName = eventList[idxEventList][1]
            method=boomFuncs.get(methName)
            # print(method)
            idxEventList += 1 
            if not method:
                method = modeFuncs.get(methName)
                if not method:
                    print("bad name - " + methName)
                else:
                    method()
            else:
                method()
                
            if idxEventList>=len(eventList):
                print("no more events in list")
                hasEvents = False
                idxEventList = 0
                
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
            if (event.key == pygame.K_s) or (event.key == pygame.K_SPACE):
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

    # are we still actively doing something, but no more events in eventList?
    if running and isActive and not hasEvents:
        # have we come to the end of any active sound too?
        if soundChannel.get_busy() == False:
            # reset, whatever we were doing is now over
            doReset()
      
    # finish off housekeeping etc      
    pygame.display.update()
    clock.tick(fps)
    
# end while run


# we have stopped running, it's time to shutdown    
print("stopped running")

shutdown()  
