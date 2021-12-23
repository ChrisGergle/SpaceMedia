import vlc
import os, time, tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import *
from time import sleep


root = Tk()
frame = tk.Frame(root, width=700, height=600)
frame.pack()

display = tk.Frame(frame, bd=5)
display.place(relwidth=1, relheight=1)

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new('StartScreen.mp4')
Media.get_mrl()
player.set_hwnd(display.winfo_id())
player.set_media(Media)
player.play()
sleep(15)

while player.is_playing():
    sleep(1)

root.update()