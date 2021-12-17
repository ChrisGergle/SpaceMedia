import vlc
import os, time
from datetime import *
import RPi.GPIO as GPIO

#Vars

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)
GPIO.setup(18,GPIO.IN)


update = True #Update to false to exit

def Main():
    # Setup logs
    print(date.today())
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
    player.set_media_list(Media_list)

    playerState = {0: 'NothingSpecial',
 1: 'Opening',
 2: 'Buffering',
 3: 'Playing',
 4: 'Paused',
 5: 'Stopped',
 6: 'Ended',
 7: 'Error'}

    subsPlayed = 0
    nosubsPlayed = 0
    active = 0
    playingMedia = 0

    while update:
        input = GPIO.input(17)
        state = str(player.get_state())

        if(state == playerState[0]):
            player.play_item_at_index(0)
    
        if(state == playerState[7]):
            player.play_item_at_index(0)
            playingMedia = 0
        
        if input == 1 and playingMedia == 0:
            playingMedia = 1
            player.play_item_at_index(1)
            active +=1
            nosubsPlayed +=1
        
        print(playingMedia)

    with open(str(date.today()))+'.txt','w' as file:
        file.write("Active Views: " + active)
        file.write("SubsPlayed: " + subsPlayed)
        file.write("No Subs Played: " + nosubsPlayed)



    




    
Main()


def stateUpdate(player, input):

