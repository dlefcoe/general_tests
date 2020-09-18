'''

example by: dlefcoe

darren@redhedge.uk
twitter: @dlefcoe

'''

import tkinter as tk
from PIL import Image, ImageTk

import os


root = tk.Tk()
root.title('RedHedge - hybrids images')
root.iconbitmap('RH_icon.ico')


# image using full path in windows
my_img = ImageTk.PhotoImage(Image.open('C:/Users/darren/OneDrive - Redhedge/code/bbg/corpHybrids/dataFolder/charts/adjusted yld curve 2020-08-10 16_20_30.png'))


my_label = tk.Label(image=my_img)
my_label.pack()




button_quit = tk.Button(root, text='Exit program', command=root.quit)
button_quit.pack()




root.mainloop()