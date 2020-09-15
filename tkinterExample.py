'''

example of tkinter for redhedge

by: Darren Lefcoe
date: 15 sep 2020

'''



import tkinter as tk

# top level main window
root = tk.Tk()

# example of a label
my_label = tk.Label(root, text='hello world')

# add item to screen (packing)
my_label.pack()


# main loop (needed to run the app)
root.mainloop()


