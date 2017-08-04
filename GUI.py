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
        SMALL_TEXT_SIZE = 11
        LARGE_TEXT_SIZE = 22

        ui_frame = Tk.Frame(self, borderwidth=self.relativePadx * .5, relief=Tk.GROOVE)
        ui_frame.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True, padx=self.relativePadx * 2,
                      pady=(0, self.relativePady * 2))
        for i in xrange(0, 3):
            if i == 0:
                ui_frame.columnconfigure(i, weight=1)
            else:
                ui_frame.columnconfigure(i, weight=100)
        for i in xrange(0, 4):
            ui_frame.rowconfigure(i, weight=1)

        des_frame = Tk.Frame(ui_frame)
        des_label = Tk.Label(des_frame, text="Description:")
        des_label.pack()
        des_label.config(font=("Arial", LARGE_TEXT_SIZE))
        des_frame.grid(row=0, column=0, sticky=Tk.E)

        sett_frame = Tk.Frame(ui_frame)
        sett_label = Tk.Label(sett_frame, text="Setting:")
        sett_label.pack()
        sett_label.config(font=("Arial", LARGE_TEXT_SIZE))
        sett_frame.grid(row=1, column=0, sticky=Tk.E)

        meas_frame = Tk.Frame(ui_frame)
        meas_label = Tk.Label(meas_frame, text="Measurement:")
        meas_label.pack()
        meas_label.config(font=("Arial", LARGE_TEXT_SIZE))
        meas_frame.grid(row=2, column=0, sticky=Tk.E)

        pow_frame = Tk.Frame(ui_frame)
        pow_label = Tk.Label(pow_frame, text="Power:")
        pow_label.pack()
        pow_label.config(font=("Arial", LARGE_TEXT_SIZE))
        pow_frame.grid(row=3, column=0, sticky=Tk.E)

        ch1_frame = Tk.Frame(ui_frame)
        ch1_label = Tk.Label(ch1_frame, text="Channel 1")
        ch1_label.pack()
        ch1_label.config(font=("Arial", LARGE_TEXT_SIZE))
        ch1_frame.grid(row=0, column=1)

        ch2_frame = Tk.Frame(ui_frame)
        ch2_label = Tk.Label(ch2_frame, text="Channel 2")
        ch2_label.pack()
        ch2_label.config(font=("Arial", LARGE_TEXT_SIZE))
        ch2_frame.grid(row=0, column=2)

        set1_frame = Tk.Frame(ui_frame)
        set_ent_frame1 = Tk.Frame(set1_frame)
        setvol1_ent = Tk.Entry(set_ent_frame1, justify="center")
        setcur1_ent = Tk.Entry(set_ent_frame1, justify="center")
        v1s = Tk.Label(set_ent_frame1, text="V", font=("Arial", LARGE_TEXT_SIZE))
        a1s = Tk.Label(set_ent_frame1, text="A", font=("Arial", LARGE_TEXT_SIZE))
        padmult = 5
        setvol1_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        v1s.pack(side=Tk.LEFT)
        a1s.pack(side=Tk.RIGHT)
        setcur1_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        voltage_lab1 = Tk.Label(set1_frame, text="Voltage", font=("Arial", LARGE_TEXT_SIZE))
        current_lab1 = Tk.Label(set1_frame, text="Current", font=("Arial", LARGE_TEXT_SIZE))
        voltage_lab1.grid(row=0, column=0)
        current_lab1.grid(row=0, column=1)
        set_ent_frame1.grid(row=1, columnspan=2)
        set1_frame.grid(row=1, column=1)

        set2_frame = Tk.Frame(ui_frame)
        set_ent_frame2 = Tk.Frame(set2_frame)
        setvol2_ent = Tk.Entry(set_ent_frame2, justify="center")
        setcur2_ent = Tk.Entry(set_ent_frame2, justify="center")
        v2s = Tk.Label(set_ent_frame2, text="V", font=("Arial", LARGE_TEXT_SIZE))
        a2s = Tk.Label(set_ent_frame2, text="A", font=("Arial", LARGE_TEXT_SIZE))
        setvol2_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        v2s.pack(side=Tk.LEFT)
        a2s.pack(side=Tk.RIGHT)
        setcur2_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        voltage_lab2 = Tk.Label(set2_frame, text="Voltage", font=("Arial", LARGE_TEXT_SIZE))
        current_lab2 = Tk.Label(set2_frame, text="Current", font=("Arial", LARGE_TEXT_SIZE))
        voltage_lab2.grid(row=0, column=0)
        current_lab2.grid(row=0, column=1)
        set_ent_frame2.grid(row=1, columnspan=2)
        set2_frame.grid(row=1, column=2)

        meas1_frame = Tk.Frame(ui_frame)
        meas_ent_frame1 = Tk.Frame(meas1_frame)
        measvol1_ent = Tk.Entry(meas_ent_frame1)
        meascur1_ent = Tk.Entry(meas_ent_frame1)
        measvol1_ent.insert(0, "6.000")
        measvol1_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        meascur1_ent.insert(0, "6.000")
        meascur1_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        v1m = Tk.Label(meas_ent_frame1, text="V", font=("Arial", LARGE_TEXT_SIZE))
        a1m = Tk.Label(meas_ent_frame1, text="A", font=("Arial", LARGE_TEXT_SIZE))
        measvol1_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        v1m.pack(side=Tk.LEFT)
        a1m.pack(side=Tk.RIGHT)
        meascur1_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        meas_ent_frame1.grid(row=0, columnspan=2)
        meas1_frame.grid(row=2, column=1)

        meas2_frame = Tk.Frame(ui_frame)
        meas_ent_frame2 = Tk.Frame(meas2_frame)
        measvol2_ent = Tk.Entry(meas_ent_frame2)
        meascur2_ent = Tk.Entry(meas_ent_frame2)
        measvol2_ent.insert(0, "6.000")
        measvol2_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        meascur2_ent.insert(0, "6.000")
        meascur2_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        v2m = Tk.Label(meas_ent_frame2, text="V", font=("Arial", LARGE_TEXT_SIZE))
        a2m = Tk.Label(meas_ent_frame2, text="A", font=("Arial", LARGE_TEXT_SIZE))
        measvol2_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        v2m.pack(side=Tk.LEFT)
        a2m.pack(side=Tk.RIGHT)
        meascur2_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        meas_ent_frame2.grid(row=0, columnspan=2)
        meas2_frame.grid(row=2, column=2)

        pow1_frame = Tk.Frame(ui_frame)
        var1 = Tk.IntVar()
        on1 = Tk.Radiobutton(pow1_frame, text="ON", font=("Arial", LARGE_TEXT_SIZE), variable=var1, value=1)
        off1 = Tk.Radiobutton(pow1_frame, text="OFF", font=("Arial", LARGE_TEXT_SIZE), variable=var1, value=2)
        on1.grid(row=0, column=0)
        off1.grid(row=0, column=1)
        pow1_frame.grid(row=3, column=1)

        pow2_frame = Tk.Frame(ui_frame)
        var2 = Tk.IntVar()
        on2 = Tk.Radiobutton(pow2_frame, text="ON", font=("Arial", LARGE_TEXT_SIZE), variable=var2, value=1)
        off2 = Tk.Radiobutton(pow2_frame, text="OFF", font=("Arial", LARGE_TEXT_SIZE), variable=var2, value=2)
        on2.grid(row=0, column=0)
        off2.grid(row=0, column=1)
        pow2_frame.grid(row=3, column=2)

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
