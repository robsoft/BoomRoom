import sys
import pygame
from pygame.locals import *

try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    import Mock.GPIO as GPIO

def GetSoundFile():
    return 'media/Bunker 6.0 test 1.wav'


# this is a bit rubbish, but make a dictionary of pointers to any local functions you will call
# in your eventList. Anything that you want to call in the main BoomRoom module is already
# available to you - just put stuff here that is only in this unit
def ModeFuncs():
    return { 
        'testtrial1' : testtrial1, 
        'testtrial2' : testtrial2}


def ModeInit(eventList):
    print("any setup for Test mode")

    # this is a list of tuples, each tuple is a time in ms from the start of the 'mode',
    # and a function call (with)
    eventList.clear()
    eventList.append(tuple((2500,'boomOne')))
    eventList.append(tuple((3500,'testtrial1')))
    eventList.append(tuple((6500,'testtrial2')))
    eventList.append(tuple((6500,'boomThree')))
    eventList.append(tuple((22500,'boomFour')))


def testtrial1():
    print("in the testtrial1 method")

def testtrial2():
    print("in the testtrial2 method")
