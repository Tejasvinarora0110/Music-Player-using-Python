import tkinter as tk
from tkinter import *
from pygame import mixer
from tkinter import ttk
import os
import random
import time

class MusicPlayer:

    def __init__(self, window ):
        self.gui=window
        self.gui.geometry('365x220')
        self.gui.title('Hits Player');
        self.gui.configure(bg='black')
        self.gui.resizable(0,0)
        self.photo1 = PhotoImage(file = r"Write the dir path")#Directory in which your icons are
        self.photo2 = PhotoImage(file = r"Write the dir path")#Directory in which your icons are
        self.photo3 = PhotoImage(file = r"Write the dir path")#Directory in which your icons are
        self.photo4= PhotoImage(file = r"Write the dir path")#Directory in which your icons are
        self.photo5 = PhotoImage(file = r"Write the dir path")#Directory in which your icons are
        self.photo6 = PhotoImage(file = r"Write the dir  path")#Directory in which your icons are
        Load = Button(window,  image=self.photo4,  width = 52,height=52, command = self.load)
        Play = Button(window, image=self.photo1,  width = 52,height=52, command =self.play)
        Pause = Button(window,image=self.photo2,width=52,height=52, command = self.pause)
        Stop = Button(window , image=self.photo3,  width = 52,height=52, command = self.stop)
        Ne = Button(window,image=self.photo5,width=52,height=52, command = self.next)
        Ba=Button(window,image=self.photo6,width=52,height=52, command = self.back)
        Load.place(x=20,y=50);Play.place(x=110,y=50);Pause.place(x=200,y=50);Stop.place(x=290,y=50);Ba.place(x=110,y=150);Ne.place(x=200,y=150)
        self.n = tk.StringVar()
        self.folder = "Write the dir path"#Directory in which your Songs are
        self.filelist = [fname for fname in os.listdir(self.folder) if fname.endswith('.mp3')]
        self.optmenu = ttk.Combobox(root,textvariable=self.n,values=self.filelist,state='readonly')
        self.optmenu.bind('<<ComboboxSelected>>',self.callback)
        self.optmenu.current(0)
        self.music_file =False
        self.playing_state = True
        self.callback=False
        self.j=0
        self.last=len(self.filelist)-1


    def callback(self,event):
        self.music_file = self.n.get()


    def back(self):#Previous song
        self.j=self.optmenu.current()
        if self.j==0:
            self.j=self.last+1
            self.j=self.optmenu.current(int(self.j)-1)
            self.music_file=self.optmenu.get()
            self.play()
        else:
            self.j=self.optmenu.current(int(self.j)-1)
            self.music_file=self.optmenu.get()
            self.play()


    def next(self):#Next song
        self.j=self.optmenu.current()
        if self.j==self.last:
            self.j=-1
            self.j=self.optmenu.current(int(self.j)+1)
            self.music_file=self.optmenu.get()
            self.play()
        else:
            self.j=self.optmenu.current(int(self.j)+1)
            self.music_file=self.optmenu.get()
            self.play()


    def load(self):#Load the song
        self.optmenu.place(x=0,y=0,width=365)
        
        
    def change(self):#Change colour
      if self.playing_state:
        d=["black","brown","red","pink","orange","green","yellow","white","blue","grey","light blue"]
        self.gui.configure(bg=random.choice(d))
        self.gui.after(200, # milliseconds
                          self.change_back)


    def change_back(self):#Change colour
        if self.playing_state:
            d=["black","brown","red","pink","orange","green","yellow","white","blue","grey","light blue"]
            self.gui.configure(bg=random.choice(d))
            self.gui.after(200, # milliseconds
                              self.change)


    def play(self):#Play
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state=True
            self.change_back()
            

    def pause(self):#Pause
        if self.playing_state:
            mixer.music.pause()
            self.playing_state=False
            self.gui.configure(bg="black")
        else:
            mixer.music.unpause()
            self.playing_state = True
            self.change_back()


    def stop(self):
        mixer.music.stop()
        self.playing_state=False
        self.gui.configure(bg="black")
root = Tk()
app= MusicPlayer(root)
root.mainloop()



