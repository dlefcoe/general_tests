'''

example by: dlefcoe

darren@redhedge.uk
twitter: @dlefcoe

the cuser cannot use pack and grid together.
ie. pack & grid are mutually exclusive.

frame lets both exist together.

'''

import tkinter as tk
from PIL import Image, ImageTk

import os


root = tk.Tk()
root.title('RedHedge - frame example')
root.iconbitmap('RH_icon.ico')

# frame added to root
frame = tk.LabelFrame(root, text='this is a frame', padx=5, pady=5)

# the frame is packed
frame.pack(padx=10, pady=10)

# buttons added to frame
b = tk.Button(frame,text='dont click here')
b2 = tk.Button(frame, text='another button')

# buttons added to grid (on frame which is packed)
b.grid(row=0,column=0)
b2.grid(row=1,column=1)



root.mainloop()



