#Parker Dean
#9/18
#Calendar

from tkinter import*
from tkinter import ttk
from tkinter import font
import calendar
import time
import datetime

def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds %60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hours = hours % 24
    #set the time zone
    current_hours = current_hours - 6
    #Set specific time period
    if current_hours >= 12:
        tag =" PM"
    else:
        tag =" AM"
    #format the output
    timex = str(current_hours) + ":" + str(current_minutes) + ":" + str( current_seconds) + tag
    #xreturn the output
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time = current_time()
    #show the time
    txt.set(time)
    # Trigger the tick after 1000ms
    root.after(1000, show_time)

#Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen",False)
root.configure(background='White')
root.bind("x", quit)
root.after(1000, show_time)

fnt= font.Font(family='Helvetica',size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="Black", background="White")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

