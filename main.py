from tkinter import *

class Player:
    def __init__(self):
        self.window = Tk()
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("300x400+800+300")
        self.window.mainloop()

Player()
