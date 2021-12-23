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
    def __init__(self, window):
        super().__init__()
        Tk.Frame.__init__(self,window)
        self['bg'] = 'black'
        self['height'] = window.winfo_screenheight()
        self['width'] = window.winfo_screenwidth()
        self['bd'] = 0
        self['container'] = True

        self.parent = window
        
        self.player = None
        self.videopanel = ttk.Frame(self.parent)
        self.canvas = Tk.Canvas(self.videopanel).pack(fill=Tk.BOTH,expand=1)

        


        

#######################################

def Main():
    # Setup logs
    print(date.today())

    subsPlayed = 0
    nosubsPlayed = 0
    active = 0
    playingMedia = 0
    Instance = vlc.Instance('-f','--inpu')
    # Media Paths
    path = "/home/pi/Videos/" #Can be changed into a file-search later but for now hard-code it
    nosubs = Instance.media_new(path+"Content-NoSubs.mp4")
    subs = Instance.media_new(path+"Content-Subtitles.mp4")
    splash = Instance.media_new(path+"StartScreen.mp4")
    

    #Set List Player
    lPlayer = Instance.media_list_player_new()
    Media_list = Instance.media_list_new()
    Media_list.add_media(splash)
    Media_list.add_media(subs)
    Media_list.add_media(nosubs)
    
    
    lPlayer.set_media_list(Media_list)
    Media_list.lock()


    playerState = ['State.NothingSpecial',
 'State.Opening',
 'State.Buffering',
 'State.Playing',
 'State.Paused',
 'State.Stopped',
 'State.Ended',
 'State.Error']

    

    while update:
        #Keeps the window updated
        window.update()

        # Run the processes of playing videos
        if(GPIO.input(17)==1): input = 1
        elif(GPIO.input(18)==1): input = 2
        state = lPlayer.get_state()


        if(str(state) == playerState[0]):
            player.play_item(splash)
            player.set_playback_mode(2)
    
        if(str(state) == playerState[6]):
            lPlayer.play_item(splash)
            playingMedia = 0
        
        try:
            if input == 1 and playingMedia == 0:
                playingMedia = 1
                lPlayer.play_item(nosubs)
                active +=1
                nosubsPlayed +=1
        except:
            pass
        
        try:
            if input == 2 and playingMedia == 0:
                playingMedia = 1
                lPlayer.play_item(subs)
                active+=1
                subsPlayed+=1
        except:
            pass


    with open(str(date.today()))+'.txt','w' as file:
        file.write("Active Views: " + active)
        file.write("SubsPlayed: " + subsPlayed)
        file.write("No Subs Played: " + nosubsPlayed)

Main()




