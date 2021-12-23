import vlc
import tkinter as tk
from tkinter import *





root = tk.Tk()

frame = tk.Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)



playerState = ['State.NothingSpecial',
 'State.Opening',
 'State.Buffering',
 'State.Playing',
 'State.Paused',
 'State.Stopped',
 'State.Ended',
 'State.Error'] #Function Object


Instance = vlc.Instance('--no-video-title-show','--mouse-hide-timeout=0')
list_player = vlc.MediaListPlayer()

media_list = Instance.media_list_new()

Media = Instance.media_new('StartScreen.mp4')
NewMedia = Instance.media_new('Content-Subtitles.mp4')
Media.get_mrl()

media_list.add_media(Media)
media_list.add_media(NewMedia)

list_player.set_media_list(media_list)

player = Instance.media_player_new()
list_player.set_media_player(player)

player.set_hwnd(display.winfo_id())
#list_player.play()

pEvents = player.event_manager()

from time import sleep

state = player.get_state() # Initialize this
tick = 0 #Data Object
loop = 0 #Data Object
m = True #Function Object


def reset():
    list_player.play_item(Media)
    return False



while True:
    root.update()   
    
    #Make a string to compare
    state = str(list_player.get_state())
    if state == playerState[0]: #This will always open the splash screen
        list_player.play()

    # Compare the string. Then check whether or not M is true or false
    if state == playerState[6]:
        print("M starts at ", m)
        if m == True: 
            #list_player.play_item(Media)
            m = reset()
            print("M is now ", m)
        elif m == False:
            list_player.play_item(NewMedia)
            m = True
            print("M is now ", m)
    else:
        continue #I think no continue broke the player. So maybe this will work

