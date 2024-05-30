import tkinter as tk


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
        self.time_frame.columnconfigure(0, weight=1)
        self.time_frame.columnconfigure(1, weight=1)
        self.time_frame.rowconfigure(0, weight=1)
        self.time_frame.rowconfigure(1, weight=1)

        self.on_time_label = tk.Label(self.time_frame, text='Enter time to start watering: ')
        self.on_time_label.grid(row=0, column=0, sticky='we')

        self.on_time_entry = tk.Entry(self.time_frame, text='Enter time to start watering: ')
        self.on_time_entry.grid(row=0, column=1, sticky='we')

        self.off_time_label = tk.Label(self.time_frame, text='Enter time to stop watering: ')
        self.off_time_label.grid(row=1, column=0, sticky='we')

        self.off_time_entry = tk.Entry(self.time_frame, text='Enter time to stop watering: ')
        self.off_time_entry.grid(row=1, column=1, sticky='we')


        self.time_frame.pack(fill='x')

        self.root.mainloop()

mainScreen()