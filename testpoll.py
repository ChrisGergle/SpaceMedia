#Match Libraries for testing
import RPi.GPIO as GPIO
import os, sys, time, signal
from subprocess import Popen
from omxplayer.player import OMXPlayer

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)