'''

example by: dlefcoe

darren@redhedge.uk
twitter: @dlefcoe

'''

import tkinter as tk
from PIL import Image, ImageTk

# import os


root = tk.Tk()
root.title('RedHedge - hybrids images')
root.iconbitmap('RH_icon.ico')


# image using full path in windows
my_img1 = ImageTk.PhotoImage(Image.open('images/adjusted yld curve 2020-08-10 16_20_30.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/adjusted yld curve 2020-08-12 16_11_24.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/adjusted yld curve 2020-08-12 16_12_47.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/meanSpreads_and_Variances 2020-08-11 11_50_22.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/XS09689133422020-08-12 10_32_48.png'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = tk.Label(root, text='image 1 of 5')

try:
    my_label = tk.Label(image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

except Exception as e:
    print('no good', e)



def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number-1])
    button_forward = tk.Button(root, text = '>>>', command=lambda: forward(image_number+1))
    button_back = tk.Button(root, text='<<<', command=lambda: backward(image_number+1)) 

    # got to end
    if image_number ==5:
        button_forward = tk.Button(root, text='>>>', state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)



def backward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = tk.Label(image=image_list[image_number-1])
    button_forward = tk.Button(root, text = '>>>', command=lambda: forward(image_number-1))
    button_back = tk.Button(root, text='<<<', command=lambda: backward(image_number-1)) 

    print(image_number)
    # got to front
    if image_number ==1:
        button_back = tk.Button(root, text='<<<', state=tk.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)



button_back = tk.Button(root, text='<<<', command=lambda: backward(), state=tk.DISABLED)
button_forward = tk.Button(root, text='>>>', command=lambda: forward(2))

button_quit = tk.Button(root, text='Exit program', command=root.quit)

button_back.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_quit.grid(row=1,column=1)


root.mainloop()



