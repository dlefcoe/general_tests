'''

example of tkinter for redhedge

by: Darren Lefcoe
date: 15 sep 2020

'''



import tkinter as tk

# top level main window
root = tk.Tk()

# example of a label
my_label1 = tk.Label(root, text='hello world').grid(row=0, column=0)
my_label2 = tk.Label(root, text='hello redHedge').grid(row=1, column=5)
my_label3 = tk.Label(root, text='  ').grid(row=1, column=3) # hacky way of spacing items on a grid


# add to grid
# my_label1.grid(row=0, column=0)
# my_label2.grid(row=1, column=0)


# pack and grid are exclusive


# main loop (needed to run the app)
root.mainloop()


