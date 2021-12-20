from tkinter import *

class RedFrame(Frame):
    def __init__(self,window):
        super().__init__()
        self["height"]=window.winfo_screenheight()
        self["width"]=window.winfo_screenwidth()
        self["relief"]=RAISED
        self["bd"]=8
        self["bg"]="red"
        

window = Tk()
window.attributes('-fullscreen',True)

frame_a = RedFrame(window)
frame_a.grid(row=0,column=0)

window.mainloop()
