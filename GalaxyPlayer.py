import vlc
import os, time
#import RPi.GPIO as GPIO

#Vars












update = True #Update to false to exit

def Main():
    
    # Media Paths
    path = "Files:///home/pi/Videos/"
    nosubs = path+"Content-NoSubs.mp4"
    subs = path+"Content-Subtitles.mp4"
    splash = path+"StartScreen.mp4"
    Instance = vlc.Instance()
    playlist = set([splash,subs,nosubs])
    url = [str(splash),str(subs),str(nosubs)] #Yes, this looks pretty redundant. Hopefully it's not.



    #Setup the player
    player = Instance.media_player_new()
    Media = Instance.media_new(url[1])
    Media_list = Instance.media_list_new(playlist)
    Media.get_mrl()
    player.set_media(Media)

    tick = 0
    while update:
        if(str(player.get_state()) == "State.NothingSpecial"):
            player.play()
        #if GPIO.input(17):
        #   Media = Instance.media_new
        tick+=1
        print(player.get_state())
    
Main()


