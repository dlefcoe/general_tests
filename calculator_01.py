'''

example of tkinter for redhedge

by: Darren Lefcoe
date: 15 sep 2020

'''


import tkinter as tk


def add_numbers(number):
    # e.delete(0)
    current = e.get()
    e.delete(0,tk.END)
    e.insert(0,str(current) + str(number))
    

def button_clear():
    e.delete(0, tk.END)
    

def button_add():
    first_number = e.get()
    global f_num
    global math_type

    math_type = 'addition'
    f_num = int(first_number)
    e.delete(0, tk.END)
    
def button_subtract():
    first_number = e.get()
    global f_num
    global math_type

    math_type = 'subtraction'
    f_num = int(first_number)
    e.delete(0, tk.END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math_type

    math_type = 'multiplication'
    f_num = int(first_number)
    e.delete(0, tk.END)


def button_divide():
    first_number = e.get()
    global f_num
    global math_type

    math_type = 'division'
    f_num = int(first_number)
    e.delete(0, tk.END)



def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math_type == 'addition':
        e.insert(0, f_num + int(second_number))
    if math_type == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math_type == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math_type == 'division':
        e.insert(0, f_num / int(second_number))


# top level main window
root = tk.Tk()
root.title('simple calc')
root.iconbitmap('RH_icon.ico')

# make buttons passing arg to fn
button_01 = tk.Button(root, text='1', padx = 30, pady=30, command=lambda: add_numbers(1))
button_02 = tk.Button(root, text='2', padx = 30, pady=30, command=lambda: add_numbers(2))
button_03 = tk.Button(root, text='3', padx = 30, pady=30, command=lambda: add_numbers(3))
button_04 = tk.Button(root, text='4', padx = 30, pady=30, command=lambda: add_numbers(4))
button_05 = tk.Button(root, text='5', padx = 30, pady=30, command=lambda: add_numbers(5))
button_06 = tk.Button(root, text='6', padx = 30, pady=30, command=lambda: add_numbers(6))
button_07 = tk.Button(root, text='7', padx = 30, pady=30, command=lambda: add_numbers(7))
button_08 = tk.Button(root, text='8', padx = 30, pady=30, command=lambda: add_numbers(8))
button_09 = tk.Button(root, text='9', padx = 30, pady=30, command=lambda: add_numbers(9))
button_00 = tk.Button(root, text='0', padx = 30, pady=30, command=lambda: add_numbers(0))

# operation buttons
button_add = tk.Button(root, text='+', padx = 30, pady=30, command=button_add)
button_subtract = tk.Button(root, text='-', padx = 30, pady=30, command=button_subtract)
button_multiply = tk.Button(root, text='*', padx = 30, pady=30, command=button_multiply)
button_divide = tk.Button(root, text='/', padx = 30, pady=30, command=button_divide)

button_equal = tk.Button(root, text='=', padx = 69, pady=30, command=button_equal)
button_clear = tk.Button(root, text='clear', padx = 60, pady=30, command=button_clear)



# add buttons to screen
button_00.grid(row=4, column=0)

button_01.grid(row=3, column=0)
button_02.grid(row=3, column=1)
button_03.grid(row=3, column=2)

button_04.grid(row=2, column=0)
button_05.grid(row=2, column=1)
button_06.grid(row=2, column=2)

button_07.grid(row=1, column=0)
button_08.grid(row=1, column=1)
button_09.grid(row=1, column=2)

button_add.grid(row=6, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)


my_label1 = tk.Label(root, text='hello world').grid(row=0, column=0)
my_label2 = tk.Label(root, text='redHedge calculator').grid(row=4, column=5)



# input box (entry box)
e = tk.Entry(root, width=35, bg='yellow', borderwidth=5)

# add to grid
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)



# main loop (needed to run the app)
root.mainloop()


