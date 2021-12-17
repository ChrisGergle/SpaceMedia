import vlc
import os, time
from datetime import *
#import RPi.GPIO as GPIO

#Vars

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(17,GPIO.IN)
#GPIO.setup(18,GPIO.IN)


update = True #Update to false to exit

def Main():
    # Setup logs
    print(date.today())
    with open(str(date.today())+'.txt','w') as file:
        file.write("words")

    file.write("Yo.")
    # Media Paths
    path = "Files:///home/pi/Videos/"
    nosubs = path+"Content-NoSubs.mp4"
    subs = path+"Content-Subtitles.mp4"
    splash = path+"StartScreen.mp4"
    Instance = vlc.Instance("-f")
    playlist = set([splash,subs,nosubs])
    url = [str(splash),str(subs),str(nosubs)] #Yes, this looks pretty redundant. Hopefully it's not.



    #Setup the player
    player = Instance.media_list_player_new()
    Media = Instance.media_new(url[1])
    Media_list = Instance.media_list_new(playlist)
    Media.get_mrl()
    player.set_media(Media)

    tick = 0
    while update:
        state = player.get_state()

        if(state == 'State.NothingSpecial'):
            player.play_item_at_index(0)
            #print("Playing Initial")
            tick +=1
        elif(state == 'State.Ended'):
            #player.play()
            tick +=1
            #print("Repeat:")
    




    
Main()



