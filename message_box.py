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
# import os


# explicit imports
# from PIL import Image, ImageTk
from tkinter import messagebox



root = tk.Tk()
root.title('RedHedge - radio button example')
root.iconbitmap('RH_icon.ico')


def popup():
    messagebox.showinfo('this is my popup', 'hello world')
    messagebox.showwarning('this is my popup', 'warn warn warn !!!')
    response = messagebox.askyesno('this is my popup', 'some question')    
    if response == 1:
        tk.Label(root, text='well done').pack()
    if response == 0:
        tk.Label(root, text='also well done...').pack()


tk.Button(root, text='popup', command=popup).pack()


root.mainloop()



