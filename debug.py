import vlc
import tkinter as tk
from tkinter import *





root = tk.Tk()

frame = tk.Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)




Instance = vlc.Instance('--input-repeat=999999','--no-video-title-show','--mouse-hide-timeout=0')
list_player = vlc.MediaListPlayer()

media_list = Instance.media_list_new()

Media = Instance.media_new('StartScreen.mp4')
NewMedia = Instance.media_new('Content-Subtitles.mp4')
Media.get_mrl()

media_list.add_media(Media)
list_player.set_media_list(media_list)

player = Instance.media_player_new()
list_player.set_media_player(player)

player.set_hwnd(display.winfo_id())
list_player.play()


from time import sleep

state = player.get_state() 
tick = 0
loop = 0
while True:
    if player.is_playing():
        root.update()
    tick+=1
    #if tick%50 == 0 : 
        #print(tick, loop)
        #print(player.get_state())
        #print(player.get_position())

    if player.get_state() == "State.Playing":
        continue
    elif player.get_state() == "State.Ended":
        print("Ended")
        
    if tick == 300:
        media_list.add_media(NewMedia)
        list_player.play_item(NewMedia)
        player.set_position(0.98)
        loop = 0
    if state != player.get_state():
        print(player.get_state())
    
    if (player.get_media() == NewMedia and loop > 0):
        list_player.play_item(Media)

    state = player.get_state()

    loop+=1
    #sleep(.01)