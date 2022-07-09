from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os
import pygame

class Player:
    def __init__(self):
        pygame.mixer.init()
        self.window = ThemedTk(theme="equilux")
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("300x440+800+300")
        self.window.config(bg="#444444")

        self.img_add = PhotoImage(file="assets/add.png")
        self.img_next = PhotoImage(file="assets/next.png")
        self.img_pause = PhotoImage(file="assets/pause.png")
        self.img_play = PhotoImage(file="assets/play.png")
        self.img_previus = PhotoImage(file="assets/previus.png")
        self.img_remove = PhotoImage(file="assets/remove.png")

        self.local = ""
        self.status = 0

        self.list = Listbox(self.window, bg="#333333", height=13, fg="gray", font="arial 12",
                            selectbackground="#6868e6")
        self.list.pack(fill=X, padx=10, pady=10)

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)

        self.remove = ttk.Button(self.frame, image=self.img_remove, command=self.delete_music)
        self.remove.grid(row=0, column=0, padx=10)

        self.add = ttk.Button(self.frame, image=self.img_add, command=self.select_music)
        self.add.grid(row=0, column=1, padx=10)

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=10)

        self.previus = ttk.Button(self.frame2, image=self.img_previus, command=self.previus_music)
        self.previus.grid(row=0, column=0)

        self.play = ttk.Button(self.frame2, image=self.img_play, command=self.play_music)
        self.play.grid(row=0, column=1)

        self.next = ttk.Button(self.frame2, image=self.img_next, command=self.next_music)
        self.next.grid(row=0, column=2)

        self.volume = ttk.Scale(self.window, from_=0, to = 1, command=self.volume_set)
        self.volume.pack(fill=X, padx=10, pady=5)

        self.window.mainloop()

    def select_music(self):
        self.local = filedialog.askdirectory()
        file = os.listdir(self.local)

        for arquivo in file:
            self.list.insert(END, str(arquivo))

    def delete_music(self):
        self.list.delete(ANCHOR)

    def next_music(self):
        try:
            index = self.list.curselection()[0] + 1
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_window("They aren't not next music.")


    def previus_music(self):
        try:
            index = self.list.curselection()[0] - 1
            self.list.select_clear(0, END)
            self.list.activate(index)
            self.list.select_set(index)
            self.list.yview(index)
        except:
            self.error_window(("They aren't not previous music."))

    def play_music(self):
        try:
            if self.status == 0:
                pygame.mixer.music.load(str(self.local) + "/" + str(self.list.get(ANCHOR)))
                pygame.mixer.music.play()
                self.play.config(image=self.img_pause)
                self.status = 1
            else:
                pygame.mixer.music.pause()
                self.play.config(image=self.img_play)
                self.status = 0
        except:
            self.error_window("Music Not Valid!")

    def error_window(self, message):
        window = Toplevel()
        window.title("ERROR")
        window.geometry("300x300+300+300")
        window.resizable(0,0)
        window.config(bg="#444444")

        text = ttk.Label(window, text=str(message), font="arial 20")
        text.pack(expand=YES)

        btn = ttk.Button(window, text="OK", command=window.destroy)
        btn.pack()

    def volume_set(self, var):
        pygame.mixer.music.set_volume(self.volume.get())


Player()
