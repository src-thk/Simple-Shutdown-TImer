from tkinter import *
import os
import time

#Defines icon, title and main widget

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

root = Tk()
root.title("Simple Shutdown Timer Lite")
root.iconbitmap(resource_path("c.ico"))
root.resizable(0,0)
#Variables

choice = IntVar()
choice.set(0)
warning = Label(root, text="Empty fields not allowed.", fg="red")

#Functions
def only_numbers(char):
    return char.isdigit()

validation = root.register(only_numbers)

def on_click():
    try:
        hour = int(h.get())*3600
        minute = int(m.get())*60
        second = int(s.get())
        warning.pack_forget()
    except:
        warning.pack()
    else:
        if choice.get() == 0:
            os.system("shutdown -s -f -t {}".format(str(hour+minute+second)))
        elif choice.get() == 1:
            os.system("shutdown -r -f -t {}".format(str(hour+minute+second)))

def on_cilick_abort():
    os.system("shutdown /a")

#Timer frame

frame = LabelFrame(root, text="Timer", padx=20, pady=20)
frame.pack(padx=5, pady=5, expand=True, fill=X)

#TIMER COMPONENT

h = Entry(frame, width=3, bd=2, validate="key", validatecommand=(validation, '%S'))
h.pack(side=LEFT)
h.insert(END, "00")
hour_label = Label(frame, text="hours", padx=5).pack(side=LEFT)

m = Entry(frame, width=3, bd=2, validate="key", validatecommand=(validation, '%S'))
m.pack(side=LEFT)
m.insert(END, "00")
minute_label = Label(frame, text="minutes", padx=5).pack(side=LEFT)

s = Entry(frame, width=3, bd=2, validate="key", validatecommand=(validation, '%S'))
s.pack(side=LEFT)
s.insert(END, "00")

second_label = Label(frame, text="seconds", padx=5).pack(side=LEFT)

text_label = Label(frame, text="from now", padx=2).pack(side=LEFT)

#Choice frame

second_frame = LabelFrame(root, text="What do you want to do?", padx=20, pady=20)
second_frame.pack(padx=5, pady=5, expand=True, fill=X)

shutdown_choice = Radiobutton(second_frame, text="Shutdown", variable=choice, value=0).pack()
restart_choice = Radiobutton(second_frame, text="Restart", variable=choice, value=1).pack()

#Execute button
button = Button(root, text="Execute it", padx=25, command=on_click).pack(side=LEFT, padx=25, pady=15)
abort_button = Button(root, text="Abort", padx=25, command=on_cilick_abort).pack(side=RIGHT, padx=25, pady=15)

root.mainloop()
