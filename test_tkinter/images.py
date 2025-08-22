'''

example by: dlefcoe

dlefcoe@gmail.com
twitter: @dlefcoe

'''

import os
import tkinter as tk
from PIL import Image, ImageTk

path_to_this_folder = os.path.dirname(__file__)
icon_image_file = os.path.join(path_to_this_folder, 'images', 'RH_icon.ico')


root = tk.Tk()
root.title('LEM Solutions - hybrids images')
root.iconbitmap(icon_image_file)


# image using full path in windows
my_img = ImageTk.PhotoImage(Image.open(icon_image_file))


my_label = tk.Label(image=my_img)
my_label.pack()


button_quit = tk.Button(root, text='Exit program', command=root.quit)
button_quit.pack()




root.mainloop()