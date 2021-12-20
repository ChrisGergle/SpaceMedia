import vlc
import os, time
from tkinter import *
from tkinter import ttk
from datetime import *
#import RPi.GPIO as GPIO

#Vars

#GPIO.setmode(GPIO.BCM)

#GPIO.setup(17,GPIO.IN)
#GPIO.setup(18,GPIO.IN)


update = True #Update to false to exit
########################################
window = Tk()
window.attributes('-fullscreen',True)

class vidFrame(Frame):
    def __init__(self):
        #
        #
        #


        
window.update()
#######################################

def Main():
    # Setup logs
    print(date.today())

    subsPlayed = 0
    nosubsPlayed = 0
    active = 0
    playingMedia = 0
    
    # Media Paths
    path = "/home/pi/Videos/" #Can be changed into a file-search later but for now hard-code it
    nosubs = vlc.Media(path+"Content-NoSubs.mp4")
    subs = vlc.Media(path+"Content-Subtitles.mp4")
    splash = vlc.Media(path+"StartScreen.mp4")
    Instance = vlc.Instance("-f")

    #Setup the player
    player = Instance.media_list_player_new()
    Media_list = Instance.media_list_new()
    Media_list.add_media(splash)
    Media_list.add_media(subs)
    Media_list.add_media(nosubs)
    player.set_media_list(Media_list)
    Media_list.lock()

    playerState = ['State.NothingSpecial',
 'State.Opening',
 'State.Buffering',
 'State.Playing',
 'State.Paused',
 'State.Stopped',
 'State.Ended',
 'State.Error']

    player.set_xwindow(window)

    while update:
        if(GPIO.input(17)==1): input = 1
        elif(GPIO.input(18)==1): input = 2
        state = player.get_state()

        if(str(state) == playerState[0]):
            player.play_item(splash)
            player.set_playback_mode(2)
    
        if(str(state) == playerState[7]):
            player.play_item(splash)
            playingMedia = 0
        
        try:
            if input == 1 and playingMedia == 0:
                playingMedia = 1
                player.play_item(nosubs)
                active +=1
                nosubsPlayed +=1
        except:
            pass
        
        try:
            if input == 2 and playingMedia == 0:
                playingMedia = 1
                player.play_item(subs)
                active+=1
                subsPlayed+=1
        except:
            pass


    with open(str(date.today()))+'.txt','w' as file:
        file.write("Active Views: " + active)
        file.write("SubsPlayed: " + subsPlayed)
        file.write("No Subs Played: " + nosubsPlayed)

Main()



playerWindow = Tk()
width_value = playerWindow.winfo_screenwidth()
height_value = playerWindow.winfo_screenheight()

playerWindow.geometry("%dx%d+0+0" % (width_value, height_value))

playerWindow.mainloop()

#class BaseContainer:
 #   def __init__(self):
 #       