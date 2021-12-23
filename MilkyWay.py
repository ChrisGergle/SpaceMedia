import vlc
import os,platform,time, tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import *
try:
    import RPi.GPIO as GPIO
except:
    print("no RPI import")


# GPIO Setup for inputs
try: 
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17,GPIO.IN)
    GPIO.setup(18,GPIO.IN)
except:
    print("Still no RPI")

# Global Variables

ps = ['State.NothingSpecial',
 'State.Opening',
 'State.Buffering',
 'State.Playing',
 'State.Paused',
 'State.Stopped',
 'State.Ended',
 'State.Error']


def embed(p,d):
    if(platform.system() == 'Windows'):
        p.set_hwnd(d.winfo_id())
    elif(platform.system() == 'Linux'):
        p.set_xwindow(d.winfo_id())

def stup(mp):
    st = str(mp.get_state())
    if st == ps[0]:
        return 0
    elif st == ps[1]:
        return 1
    elif st == ps[2]:
        return 2
    elif st == ps[3]:
        return 3
    elif st == ps[4]:
        return 4
    elif st == ps[5]:
        return 5
    elif st == ps[6]:
        return 6
    elif st == ps[7]:
        return 7

##########################################
# Build the structures. For some reason it hates being a function
##########################################
### Build the screen, Fullscreen no border black background.
w = tk.Tk()
w.attributes('-fullscreen',True)
f = tk.Frame(w,width=w.winfo_screenwidth(),height=w.winfo_screenheight())
f.pack()

d = tk.Frame(w,bg='black',bd=0)
d.place(relwidth=1,relheight=1)

### Set our instance
i = vlc.Instance('--mouse-hide-timeout=0')

### Establish the media to be imported. This is hard-coded for pi, but can be adjusted later
path = "/home/pi/Videos/"
Nos = i.media_new(path+"Content-NoSubs.mp4")
Sub = i.media_new(path+"Content-Subtitles.mp4")
Start = i.media_new(path+"StartScreen.mp4")

### Set our media player up and embed it
mlp = vlc.MediaListPlayer()
ml = i.media_list_new()
mp = i.media_player_new()

mlp.set_media_player(mp)
embed(mp,d)

## Set our media list up
ml.add_media(Start)
ml.add_media(Sub)
ml.add_media(Nos)


def main():

    ### Build the screen, Fullscreen no border black background.
    w = tk.Tk()
    w.attributes('-fullscreen',True)
    f = tk.Frame(w,width=w.winfo_screenwidth(),height=w.winfo_screenheight())
    f.pack()

    d = tk.Frame(w,bg='black',bd=0)
    d.place(relwidth=1,relheight=1)

    ### Set our instance
    i = vlc.Instance('--mouse-hide-timeout=0')

    ### Establish the media to be imported. This is hard-coded for pi, but can be adjusted later
    path = "/home/pi/Videos/"
    Nos = i.media_new(path+"Content-NoSubs.mp4")
    Sub = i.media_new(path+"Content-Subtitles.mp4")
    Start = i.media_new(path+"StartScreen.mp4")

    ### Set our media player up and embed it
    mlp = vlc.MediaListPlayer()
    ml = i.media_list_new()
    mp = i.media_player_new()
    
    mlp.set_media_player(mp)
    embed(mp,d)
    
    ## Set our media list up
    ml.add_media(Start)
    ml.add_media(Sub)
    ml.add_media(Nos)

    ### Loop variables
    update = True
    active = False #Starts Inactive. Someone needs to push the button.
    a = 0   #Input A
    b = 0   #Input B
    Loop = 0
    Novid=0
    cSub = 0
    cNos = 0
    st = 0

    while update==True:
        ### Main loop
        w.update()
        st = stup(mp)
        #print(st)
        
        ### Checks the number of times the button is actually pressed
        ### This is strictly data collection and may help with button lifespan checks
        try:
            inA = GPIO.input(17)
            inB = GPIO.input(18)
            
            if GPIO.input(17) != inA and GPIO.input(17) == 1:
                a+=1 
            if GPIO.input(18) != inB and GPIO.input(18) == 1:
                b+=1
        except:
            print("Button Press: GPIO not existant on system")


        ### Player is Nothing Special
        if active == False and st == 0:
            mlp.play_item(Start)
            Loop+=1
            Novid+=1

        ### Player is Playing
        if st==4:
            if active == True:
               continue
            elif active == False:
                try:
                    if GPIO.input(17) == 1 and GPIO.input(18)==0:
                        mlp.play_item(Nos)
                        active = True
                        cNos+=1
                        Loop+=1
                    if GPIO.input(18) == 1:
                        mlp.play_item(Sub)
                        active = True
                        cSub+=1
                        Loop+=1
                except:
                    print("no GPIO")

        if st == 4 and active == True:
            mlp.play_item(Start)
            active = False 
            Loop+=1
            Novid+=1


        ### Player is Ended
        if st == 6:
            try:
                if GPIO.input(17) == 1 and GPIO.input(18)==0:
                    mlp.play_item(Nos)
                    active = True
                    cNos+=1
                    Loop+=1
                if GPIO.input(18) == 1:
                    mlp.play_item(Sub)
                    active = True
                    cSub+=1
                    Loop+=1
                if GPIO.input(17) == 0 and GPIO.input(18)==0:
                    mlp.play_item(Start)
                    Loop+1
                    Novid+=1
            except:
                mlp.play_item(Start)
                Loop+1
                Novid+=1
                print("no GPIO")


        
        

main()