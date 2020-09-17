'''

example of tkinter for redhedge

by: Darren Lefcoe
date: 15 sep 2020

'''



import tkinter as tk

# top level main window
root = tk.Tk()

# example of a label
my_label1 = tk.Label(root, text='hello world')
my_label2 = tk.Label(root, text='hello redHedge')


# add to grid
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)


# pack and grid are exclusive


# main loop (needed to run the app)
root.mainloop()


