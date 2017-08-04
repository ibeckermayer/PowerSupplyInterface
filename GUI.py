"""
Code modified largely from: http://zetcode.com/gui/tkinter/
"""

import Tkinter as Tk


class GUI(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)

        self.parent = parent
        self.screenwidth = self.parent.winfo_screenwidth()
        self.screenheight = self.parent.winfo_screenheight()
        self.relativePadx = self.screenwidth / 384.
        self.relativePady = self.screenheight / 240.

        self.parent.title("Power Supply Interface")  # master gives access to the root window (Tk)
        self.pack(fill=Tk.BOTH, expand=1)  # put our Frame on entire Tk window
        self.center_window()

        self.UIwidth = self.winfo_width()
        self.UIheight = self.winfo_height()

        self.init_gui()

    def init_gui(self):
        self.create_label_frame()
        self.create_ui_frame()

    def create_label_frame(self):
        # Create the main frame for the label
        label_frame = Tk.Frame(self, borderwidth=self.relativePadx * .5, relief=Tk.GROOVE)
        label_frame.pack(side=Tk.TOP, fill=Tk.X, padx=self.relativePadx * 2,
                         pady=(self.relativePady, self.relativePady))
        # Create "POWER SUPPLY:"
        ps_lab = Tk.Label(label_frame, text="POWER SUPPLY:")
        ps_lab.pack(side=Tk.LEFT, padx=self.relativePadx * 5)
        ps_lab.config(font=("Arial", 22))
        # Create name of the power supply
        name_lab = Tk.Label(label_frame, text="BK PRECISION 9173")
        name_lab.place(relx=0.5, rely=0.5, anchor=Tk.CENTER)
        name_lab.config(font=("Arial", 22))

        # Create separate frame for the IP ADDRESS label and entry box
        ipFrame = Tk.Frame(label_frame)
        ipFrame.pack(side=Tk.RIGHT, pady=self.relativePady * 2)
        ip_lab = Tk.Label(ipFrame, text="IP ADDRESS")
        ip_lab.pack(side=Tk.TOP)  # , anchor=tk.E, padx=self.relativePadx*5)
        ip_lab.config(font=("Arial", 22))
        ip = Tk.Entry(ipFrame)
        ip.insert(0, "142.103.235.210")
        ip.configure(state='readonly', font=("Arial", 14), justify="center")
        ip.pack(side=Tk.BOTTOM, anchor=Tk.E, padx=self.relativePadx * 5)

    def create_ui_frame(self):
        ui_frame = Tk.Frame(self, borderwidth=self.relativePadx * .5, relief=Tk.GROOVE)
        ui_frame.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True, padx=self.relativePadx * 2,
                      pady=(0, self.relativePady * 2))
        for i in xrange(0, 3):
            if i==0:
                ui_frame.columnconfigure(i, weight=1)
            else:
                ui_frame.columnconfigure(i, weight=100)
        for i in xrange(0, 4):
            ui_frame.rowconfigure(i, weight=1)

        des_frame = Tk.Frame(ui_frame)
        des_label = Tk.Label(des_frame, text="Description:")
        des_label.pack()
        des_label.config(font=("Arial", 22))
        des_frame.grid(row=0, column=0, sticky=Tk.E)

        sett_frame = Tk.Frame(ui_frame)
        sett_label = Tk.Label(sett_frame, text="Setting:")
        sett_label.pack()
        sett_label.config(font=("Arial", 22))
        sett_frame.grid(row=1, column=0, sticky=Tk.E)

        meas_frame = Tk.Frame(ui_frame)
        meas_label = Tk.Label(meas_frame, text="Measurement:")
        meas_label.pack()
        meas_label.config(font=("Arial", 22))
        meas_frame.grid(row=2, column=0, sticky=Tk.E)

        pow_frame = Tk.Frame(ui_frame)
        pow_label = Tk.Label(pow_frame, text="Power:")
        pow_label.pack()
        pow_label.config(font=("Arial", 22))
        pow_frame.grid(row=3, column=0, sticky=Tk.E)

        ch1_frame = Tk.Frame(ui_frame)
        ch1_label = Tk.Label(ch1_frame, text="Channel 1")
        ch1_label.pack()
        ch1_label.config(font=("Arial", 22))
        ch1_frame.grid(row=0, column=1)

        ch2_frame = Tk.Frame(ui_frame)
        ch2_label = Tk.Label(ch2_frame, text="Channel 2")
        ch2_label.pack()
        ch2_label.config(font=("Arial", 22))
        ch2_frame.grid(row=0, column=2)

    def center_window(self):
        w = self.screenwidth / 1.5
        h = self.screenheight / 1.8
        x = (self.screenwidth - w) / 2
        y = (self.screenheight - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk.Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
