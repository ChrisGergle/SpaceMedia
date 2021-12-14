import RPi.GPIO as GPIO
import os, sys, time, signal, vlc
from subprocess import Popen
try:
    import pynput
except:
    print("Keyboard not Imported.")
try:
    from omxplayer.player import OMXPlayer
except:
    print("oxmplayer library not imported")

# Mandatory Settings

GPIO.setmmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)
GPIO.setup(18,GPIO.IN)


# Establish Variables needed
btn1 = False
btn2 = False


def btnPress(num):
    if num == 1:
        btn1 = True
    elif num == 2:
        btn2 = True

# State Machine to launch
def Main():
    
    ### Variables
    pressedAtStart = False
    
    # Video selections
    openVid = ""
    startScreen = "/home/pi/videos/StartScreen.mp4"
    subs = "/home/pi/videos/Content-Subtitles.mp4"
    nosubs = "/home/pi/videos/Content-NoSubs.mp4"
    
    runTime = 0
    active = False
    player = False
    
    #Check for buttons pressed at start
    if GPIO.input(17) is True or GPIO.input(18) is True:
        print("Button is pressed during startup.")
        print ("17 is pressed? " + GPIO.input(17))
        print ("18 is pressed? " + GPIO.input(18))
        pressedAtStart = True
    else:
        pressedAtStart = False

    while True:
        
        if active is True:


        #If Esc is pressed, exit.
        #end loop
    #end Main()





    
Main()

    




# Garbage Collection
GPIO.cleanup()