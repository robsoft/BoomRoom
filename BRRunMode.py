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
    return 'media/Boom Room 1 LR.wav'

# this is a bit rubbish, but make a dictionary of pointers to any local functions you will call
# in your eventList. Anything that you want to call in the main BoomRoom module is already
# available to you - just put stuff here that is only in this unit
def ModeFuncs():
    return { 
        'runtrial1' : runtrial1, 
        'runtrial2' : runtrial2}


def ModeInit(eventList):
    print("any setup for Run mode")

    # this is a list of tuples, each tuple is a time in ms from the start of the 'mode',
    # and a function call (with)
    eventList.clear()
    eventList.append(tuple((1500,'boomOne')))
    eventList.append(tuple((3500,'boomTwo')))
    eventList.append(tuple((3500,'runtrial1')))
    eventList.append(tuple((6500,'boomFour')))
    eventList.append(tuple((12500,'runtrial2')))
    eventList.append(tuple((22500,'boomThree')))

def runtrial1():
    print("in the runtrial1 method")

def runtrial2():
    print("in the runtrial2 method")