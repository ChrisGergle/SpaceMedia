import vlc
import os, time
from tkinter import *
from tkinter import ttk
from datetime import *
class playerFrame(Frame):
    def __init__(self,window):
        super().__init__()
        self["height"]=window.winfo_screenheight()
        self["width"]=window.winfo_screenwidth()
        self["relief"]=FLAT
        self["bd"]=0
        self["bg"]="black"
        self["container"]=True
        
def window():
    window = Tk()
    window.attributes('-fullscreen',True)

    frame_a = playerFrame(window)
    frame_a.grid(row=0,column=0)

    return window

def main():
    # Set up the window
    view = window()
    frame =     
    Instance = vlc.Instance() #instantiate vlc for use
    
    player = Instance.media_player_new()
    player.set_xwindow(view.Frame(playerFrame))


    path = "/home/pi/Videos/" #Can be changed into a file-search later but for now hard-code it

    nosubs = vlc.Media(path+"Content-NoSubs.mp4")
    subs = vlc.Media(path+"Content-Subtitles.mp4")
    splash = vlc.Media(path+"StartScreen.mp4")

    

    
    while True:
        view.update()

main()