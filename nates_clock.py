import tkinter as tk
import time


def update_clock():
    current_time = time.strftime('%H:%M:%S')
    # Alternate color every second
    second = int(time.strftime('%S'))
    color = 'red' if second % 2 == 0 else 'lime'
    label.config(text=current_time, fg=color)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Clock")

label = tk.Label(root, font=('Arial', 48), bg='black', fg='lime')
label.pack(padx=20, pady=20)

update_clock()
root.mainloop()
