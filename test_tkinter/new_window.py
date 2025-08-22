'''

example by: dlefcoe

darren@redhedge.uk
twitter: @dlefcoe

the cuser cannot use pack and grid together.
ie. pack & grid are mutually exclusive.

frame lets both exist together.

'''

# imports
import tkinter as tk
import os

# explicit imports
from PIL import Image, ImageTk
from tkinter import messagebox


root = tk.Tk()
root.title('RedHedge - multiple window example')
root.iconbitmap('RH_icon.ico')

def open_window():
    global my_image
    top = tk.Toplevel()
    top.title('the second window')
    top.iconbitmap('RH_icon.ico')

    tk.Label(top, text='hello world').pack()
    tk.Label(root,text='the main one').pack()

    tk.Button(top, text='close window', command=top.destroy).pack()


    my_image = ImageTk.PhotoImage(Image.open('images/adjusted yld curve 2020-08-12 13_17_53.png'))
    tk.Label(top, image=my_image ).pack()

button = tk.Button(root, text='open the second window', command=open_window)
button.pack()


root.mainloop()



