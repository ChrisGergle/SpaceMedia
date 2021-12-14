import vlc
import os, time
#import RPi.GPIO as GPIO

#Vars
path = "Files:///home/pi/Videos/"
nosubs = path+"Content-NoSubs.mp4"
subs = path+"Content-Subtitles.mp4"
splash = path+"StartScreen.mp4"

url = [str(splash),str(subs),str(nosubs)] #Yes, this looks pretty redundant. Hopefully it's not.


#Set up Playing Status Values
playing = set([1,2,3,4])

Instance = vlc.Instance()

playlist = set([splash,subs,nosubs])


def Main():
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media_list = Instance.media_list_new([url])



Main()    


