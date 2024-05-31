import tkinter as tk
from tkinter import ttk


class mainScreen:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry('800x400')
        self.root.title('AutoWater')


        #  Title label
        self.title = tk.Label(self.root, text='AutoWater', font=('Montserrat', 28), bg='#17bf9b')
        self.title.pack(fill='x')

        #  Manual on and off buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)
        self.on_button = tk.Button(self.button_frame, text='Water On', font=('Montserrat', 20), bg='#32a852')
        self.on_button.grid(row=0, column=0, sticky='we', ipady=20)
        self.off_button = tk.Button(self.button_frame, text='Water Off', font=('Montserrat', 20), bg='#bf1717')
        self.off_button.grid(row=0, column=1, sticky='we', ipady=20)
        self.button_frame.pack(fill='x')

        #  Time entries
        self.time_frame = tk.Frame(self.root)
        self.time_frame.columnconfigure(0, weight=3)
        self.time_frame.columnconfigure(1, weight=1)
        self.time_frame.columnconfigure(2, weight=1)
        self.on_time_label = tk.Label(self.time_frame, text='Enter time to start watering: ', font=('Montserrat', 14))
        self.on_time_label.grid(row=0, column=0, sticky='nsew')
        def create_hrs_list():
            hrs_list = []
            for i in range(24):
                hrs_list.append(i)
            return hrs_list
        self.hr_dropdown = ttk.Combobox(self.time_frame, state='readonly', values=create_hrs_list(), font=('Montserrat', 14), width=3)
        self.hr_dropdown.grid(row=0, column=1, sticky='nsew')
        def create_minutes_list():
            minutes_list = []
            for i in range(60):
                minutes_list.append(i)
            return minutes_list
        self.min_dropdown = ttk.Combobox(self.time_frame, state='readonly', values=create_minutes_list(), font=('Montserrat', 14), width=3)
        self.min_dropdown.grid(row=0, column=2, sticky='nsew')
        self.time_frame.pack(fill='x')

        # Water volume entry
        self.volume_frame = tk.Frame(self.root)
        self.volume_frame.columnconfigure(0, weight=3)
        self.volume_frame.columnconfigure(1, weight=1)
        self.volume_frame.columnconfigure(2, weight=1)
        self.volume_label = tk.Label(self.volume_frame, text='Set water volume to dispense: ', font=('Montserrat', 14))
        self.volume_label.grid(row=0, column=0, sticky='nsew')
        self.volume_entry = tk.Entry(self.volume_frame, font=('Montserrat', 14))
        self.volume_entry.grid(row=0, column=1, sticky='nsew')
        self.volume_label_unit = tk.Label(self.volume_frame, text='ml', font=('Montserrat', 14))
        self.volume_label_unit.grid(row=0, column=2, sticky='nsew')
        self.volume_frame.pack(fill='x')


        self.root.mainloop()

mainScreen()