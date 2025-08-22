import tkinter as tk
import pytz
from tkinter import Menu, StringVar
from datetime import datetime


class ClockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock")
        self.label = tk.Label(self.root, font=("Arial", 48), bg="black", fg="lime")
        self.label.pack(padx=20, pady=20)

        # Display current timezone
        self.timezone_var = StringVar(value="UTC")
        self.timezone_label = tk.Label(
            self.root, text=f"Timezone: {self.timezone_var.get()}", font=("Arial", 14)
        )
        self.timezone_label.pack(pady=(0, 10))

        self.timezones = sorted(pytz.all_timezones)

        # Search box for timezones
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=(0, 10))
        tk.Label(search_frame, text="Search Timezone:").pack(side=tk.LEFT)
        self.search_var = StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT)
        self.search_entry.bind("<KeyRelease>", self.on_search)

        # Listbox for filtered timezones
        self.listbox = tk.Listbox(self.root, height=8, width=40)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_listbox_select)
        self.update_listbox(self.timezones)

        # Menubar
        menubar = Menu(self.root)
        timezone_menu = Menu(menubar, tearoff=0)
        for tz in self.timezones:
            timezone_menu.add_radiobutton(
                label=tz,
                variable=self.timezone_var,
                value=tz,
                command=self.update_clock,
            )
        menubar.add_cascade(label="Timezone", menu=timezone_menu)
        self.root.config(menu=menubar)

    def update_listbox(self, timezones):
        self.listbox.delete(0, tk.END)
        for tz in timezones:
            self.listbox.insert(tk.END, tz)

    def on_search(self, event=None):
        search_term = self.search_var.get()
        filtered = self.search_timezones(search_term)
        self.update_listbox(filtered)

    def on_listbox_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            tz = self.listbox.get(selection[0])
            self.timezone_var.set(tz)
            self.update_clock()

    def search_timezones(self, search_term: str) -> list[str]:
        """Search for timezones containing the search term."""
        return [tz for tz in self.timezones if search_term.lower() in tz.lower()]

    def update_clock(self) -> None:
        tz = pytz.timezone(self.timezone_var.get())
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M:%S")
        second = now.second
        color = "red" if second % 2 == 0 else "lime"
        self.label.config(text=current_time, fg=color)
        self.timezone_label.config(text=f"Timezone: {self.timezone_var.get()}")
        self.root.after(1000, self.update_clock)

    def run(self):
        self.update_clock()
        self.root.mainloop()


def main():
    app = ClockApp()
    app.run()


if __name__ == "__main__":
    main()
