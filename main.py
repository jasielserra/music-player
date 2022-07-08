from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

class Player:
    def __init__(self):
        self.window = ThemedTk(theme="equilux")
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("300x400+800+300")
        self.window.config(bg="#333333")

        self.list = Listbox(self.window, bg="#444444")
        self.list.pack(fill=X, padx=10, pady=10)

        self.window.mainloop()

Player()
