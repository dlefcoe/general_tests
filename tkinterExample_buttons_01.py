'''

example of tkinter for redhedge

by: Darren Lefcoe
date: 15 sep 2020

'''


import tkinter as tk


def myClick():
    my_label = tk.Label(root, text='user clicked a button')    
    my_label.grid(row=0,column=1)

# top level main window
root = tk.Tk()

# example of a label
my_label1 = tk.Label(root, text='hello world').grid(row=0, column=0)
my_label2 = tk.Label(root, text='hello redHedge').grid(row=3, column=5)

# add button with padding and foreground & background colours
my_button = tk.Button(root, text='click me', padx=50, pady=20, command=myClick, fg='blue', bg='white')

# add to grid
my_button.grid(row=1, column=2)





# main loop (needed to run the app)
root.mainloop()


