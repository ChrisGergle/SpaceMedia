import moviepy
from moviepy.editor import *
import pygame
import sys
import time

pygame.init()


clip = VideoFileClip('StartScreen.mp4').resize((1280,720))


Update = True
x = 0

while Update:
    clip.show(interactive = True)
    x+=1
    if(x > 10):
        Update = False

pygame.quit()