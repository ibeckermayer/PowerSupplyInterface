"""
Useful links to understand the code:
http://zetcode.com/gui/tkinter/
http://effbot.org/tkinterbook/
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://stackoverflow.com/questions/24832247/constantly-update-label-widgets-from-entry-widgets-tkinter
"""

import Tkinter as Tk
import Queue as Q
from PowerSupplies import BKPRECISION9173 as Bkp


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class GUI(Tk.Frame):
    def __init__(self, parent, power_supply):
        Tk.Frame.__init__(self, parent)
        self.update_time_ms = 100  # update measurements every X ms

        self.bkp = power_supply
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
        self.label_frame = Tk.Frame(self, borderwidth=self.relativePadx * .5, relief=Tk.GROOVE)
        self.label_frame.pack(side=Tk.TOP, fill=Tk.X, padx=self.relativePadx * 2,
                              pady=(self.relativePady, self.relativePady))
        # Create "POWER SUPPLY:"
        self.ps_lab = Tk.Label(self.label_frame, text="POWER SUPPLY:")
        self.ps_lab.pack(side=Tk.LEFT, padx=self.relativePadx * 5)
        self.ps_lab.config(font=("Arial", 22))
        # Create name of the power supply
        self.name_lab = Tk.Label(self.label_frame, text=self.bkp.name)
        self.name_lab.place(relx=0.5, rely=0.5, anchor=Tk.CENTER)
        self.name_lab.config(font=("Arial", 22))

        # Create separate frame for the IP ADDRESS label and entry box
        self.ipFrame = Tk.Frame(self.label_frame)
        self.ipFrame.pack(side=Tk.RIGHT, pady=self.relativePady * 2)
        self.ip_lab = Tk.Label(self.ipFrame, text="IP ADDRESS")
        self.ip_lab.pack(side=Tk.TOP)  # , anchor=tk.E, padx=self.relativePadx*5)
        self.ip_lab.config(font=("Arial", 22))
        self.ip = Tk.Entry(self.ipFrame)
        self.ip.insert(0, self.bkp.host)
        self.ip.configure(state='readonly', font=("Arial", 14), justify="center")
        self.ip.pack(side=Tk.BOTTOM, anchor=Tk.E, padx=self.relativePadx * 5)

    def create_ui_frame(self):
        SMALL_TEXT_SIZE = 11
        LARGE_TEXT_SIZE = 22

        self.ui_frame = Tk.Frame(self, borderwidth=self.relativePadx * .5, relief=Tk.GROOVE)
        self.ui_frame.pack(side=Tk.TOP, fill=Tk.BOTH, expand=True, padx=self.relativePadx * 2,
                           pady=(0, self.relativePady * 2))
        for i in xrange(0, 3):
            if i == 0:
                self.ui_frame.columnconfigure(i, weight=1)
            else:
                self.ui_frame.columnconfigure(i, weight=100)
        for i in xrange(0, 4):
            self.ui_frame.rowconfigure(i, weight=1)

        self.des_frame = Tk.Frame(self.ui_frame)
        self.des_label = Tk.Label(self.des_frame, text="Description:")
        self.des_label.pack()
        self.des_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.des_frame.grid(row=0, column=0, sticky=Tk.E)

        self.sett_frame = Tk.Frame(self.ui_frame)
        self.sett_label = Tk.Label(self.sett_frame, text="Setting:")
        self.sett_label.pack()
        self.sett_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.sett_frame.grid(row=1, column=0, sticky=Tk.E)

        self.meas_frame = Tk.Frame(self.ui_frame)
        self.meas_label = Tk.Label(self.meas_frame, text="Measurement:")
        self.meas_label.pack()
        self.meas_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.meas_frame.grid(row=2, column=0, sticky=Tk.E)

        self.pow_frame = Tk.Frame(self.ui_frame)
        self.pow_label = Tk.Label(self.pow_frame, text="Power:")
        self.pow_label.pack()
        self.pow_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.pow_frame.grid(row=3, column=0, sticky=Tk.E)

        self.ch1_frame = Tk.Frame(self.ui_frame)
        self.ch1_label = Tk.Label(self.ch1_frame, text="Channel 1")
        self.ch1_label.pack()
        self.ch1_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.ch1_frame.grid(row=0, column=1)

        self.ch2_frame = Tk.Frame(self.ui_frame)
        self.ch2_label = Tk.Label(self.ch2_frame, text="Channel 2")
        self.ch2_label.pack()
        self.ch2_label.config(font=("Arial", LARGE_TEXT_SIZE))
        self.ch2_frame.grid(row=0, column=2)

        self.vol1ent = Tk.StringVar()  # create string variables for the entries
        self.cur1ent = Tk.StringVar()
        self.set1_frame = Tk.Frame(self.ui_frame)
        self.set_ent_frame1 = Tk.Frame(self.set1_frame)
        self.setvol1_ent = Tk.Entry(self.set_ent_frame1, justify="center", textvariable=self.vol1ent)
        self.setvol1_ent.insert(0, self.bkp.voltageSetting1)
        self.setvol1_ent.bind("<Return>", lambda event: self.update_vol1(event))  # bind entry to return key
        self.setcur1_ent = Tk.Entry(self.set_ent_frame1, justify="center", textvariable=self.cur1ent)
        self.setcur1_ent.insert(0, self.bkp.currentSetting1)
        self.setcur1_ent.bind("<Return>", lambda event: self.update_cur1(event))
        self.v1s = Tk.Label(self.set_ent_frame1, text="V", font=("Arial", LARGE_TEXT_SIZE))
        self.a1s = Tk.Label(self.set_ent_frame1, text="A", font=("Arial", LARGE_TEXT_SIZE))
        padmult = 5
        self.setvol1_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        self.v1s.pack(side=Tk.LEFT)
        self.a1s.pack(side=Tk.RIGHT)
        self.setcur1_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        self.voltage_lab1 = Tk.Label(self.set1_frame, text="Voltage", font=("Arial", LARGE_TEXT_SIZE))
        self.current_lab1 = Tk.Label(self.set1_frame, text="Current", font=("Arial", LARGE_TEXT_SIZE))
        self.voltage_lab1.grid(row=0, column=0)
        self.current_lab1.grid(row=0, column=1)
        self.set_ent_frame1.grid(row=1, columnspan=2)
        self.set1_frame.grid(row=1, column=1)

        self.vol2ent = Tk.StringVar()  # create string variables for the entries
        self.cur2ent = Tk.StringVar()
        self.set2_frame = Tk.Frame(self.ui_frame)
        self.set_ent_frame2 = Tk.Frame(self.set2_frame)
        self.setvol2_ent = Tk.Entry(self.set_ent_frame2, justify="center", textvariable=self.vol2ent)
        self.setvol2_ent.insert(0, self.bkp.voltageSetting2)
        self.setvol2_ent.bind("<Return>", lambda event: self.update_vol2(event))  # bind entry to return key
        self.setcur2_ent = Tk.Entry(self.set_ent_frame2, justify="center", textvariable=self.cur2ent)
        self.setcur2_ent.insert(0, self.bkp.currentSetting2)
        self.setcur2_ent.bind("<Return>", lambda event: self.update_cur2(event))  # bind entry to return key
        self.v2s = Tk.Label(self.set_ent_frame2, text="V", font=("Arial", LARGE_TEXT_SIZE))
        self.a2s = Tk.Label(self.set_ent_frame2, text="A", font=("Arial", LARGE_TEXT_SIZE))
        self.setvol2_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        self.v2s.pack(side=Tk.LEFT)
        self.a2s.pack(side=Tk.RIGHT)
        self.setcur2_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        self.voltage_lab2 = Tk.Label(self.set2_frame, text="Voltage", font=("Arial", LARGE_TEXT_SIZE))
        self.current_lab2 = Tk.Label(self.set2_frame, text="Current", font=("Arial", LARGE_TEXT_SIZE))
        self.voltage_lab2.grid(row=0, column=0)
        self.current_lab2.grid(row=0, column=1)
        self.set_ent_frame2.grid(row=1, columnspan=2)
        self.set2_frame.grid(row=1, column=2)

        self.meas1_frame = Tk.Frame(self.ui_frame)
        self.meas_ent_frame1 = Tk.Frame(self.meas1_frame)
        self.measvol1_ent = Tk.Entry(self.meas_ent_frame1)
        self.meascur1_ent = Tk.Entry(self.meas_ent_frame1)
        self.measvol1_ent.insert(0, self.bkp.voltageMeasured1)
        self.measvol1_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        self.meascur1_ent.insert(0, self.bkp.currentMeasured1)
        self.meascur1_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        self.v1m = Tk.Label(self.meas_ent_frame1, text="V", font=("Arial", LARGE_TEXT_SIZE))
        self.a1m = Tk.Label(self.meas_ent_frame1, text="A", font=("Arial", LARGE_TEXT_SIZE))
        self.measvol1_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        self.v1m.pack(side=Tk.LEFT)
        self.a1m.pack(side=Tk.RIGHT)
        self.meascur1_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        self.meas_ent_frame1.grid(row=0, columnspan=2)
        self.meas1_frame.grid(row=2, column=1)

        self.meas2_frame = Tk.Frame(self.ui_frame)
        self.meas_ent_frame2 = Tk.Frame(self.meas2_frame)
        self.measvol2_ent = Tk.Entry(self.meas_ent_frame2)
        self.meascur2_ent = Tk.Entry(self.meas_ent_frame2)
        self.measvol2_ent.insert(0, self.bkp.voltageMeasured2)
        self.measvol2_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        self.meascur2_ent.insert(0, self.bkp.currentMeasured2)
        self.meascur2_ent.configure(state='readonly', font=("Arial", SMALL_TEXT_SIZE), justify="center")
        self.v2m = Tk.Label(self.meas_ent_frame2, text="V", font=("Arial", LARGE_TEXT_SIZE))
        self.a2m = Tk.Label(self.meas_ent_frame2, text="A", font=("Arial", LARGE_TEXT_SIZE))
        self.measvol2_ent.pack(side=Tk.LEFT, padx=(self.relativePadx * padmult, 0))
        self.v2m.pack(side=Tk.LEFT)
        self.a2m.pack(side=Tk.RIGHT)
        self.meascur2_ent.pack(side=Tk.RIGHT, padx=(self.relativePadx * padmult, 0))
        self.meas_ent_frame2.grid(row=0, columnspan=2)
        self.meas2_frame.grid(row=2, column=2)

        self.pow1_frame = Tk.Frame(self.ui_frame)
        self.var1 = Tk.IntVar()  # must be a class variable in order to stay around after the function call
        self.on1 = Tk.Radiobutton(self.pow1_frame, text="ON", font=("Arial", LARGE_TEXT_SIZE), variable=self.var1,
                                  value=1, command=self.onoff1)
        self.off1 = Tk.Radiobutton(self.pow1_frame, text="OFF", font=("Arial", LARGE_TEXT_SIZE), variable=self.var1,
                                   value=2, command=self.onoff1)
        self.on1.grid(row=0, column=0)
        self.off1.grid(row=0, column=1)
        if self.bkp.chan1on:
            self.var1.set(1)
        else:
            self.var1.set(2)
            self.pow1_frame.grid(row=3, column=1)

        self.pow2_frame = Tk.Frame(self.ui_frame)
        self.var2 = Tk.IntVar()  # must be a class variable in order to stay around after the function call
        self.on2 = Tk.Radiobutton(self.pow2_frame, text="ON", font=("Arial", LARGE_TEXT_SIZE), variable=self.var2,
                                  value=1, command=self.onoff2)
        self.off2 = Tk.Radiobutton(self.pow2_frame, text="OFF", font=("Arial", LARGE_TEXT_SIZE), variable=self.var2,
                                   value=2, command=self.onoff2)
        self.on2.grid(row=0, column=0)
        self.off2.grid(row=0, column=1)
        if self.bkp.chan2on:
            self.var2.set(1)
        else:
            self.var2.set(2)
        self.pow2_frame.grid(row=3, column=2)

    def update_vol1(self, key):
        self.bkp.set_voltage(1, self.vol1ent.get())

    def update_vol2(self, key):
        self.bkp.set_voltage(2, self.vol2ent.get())

    def update_cur1(self, key):
        self.bkp.set_current(1, self.cur1ent.get())

    def update_cur2(self, key):
        self.bkp.set_current(2, self.cur2ent.get())

    def update_measurements(self):
        """
Looping function to update the measurement readings every update_time_ms milliseconds
        """
        self.bkp.measure_current(1)
        self.bkp.measure_current(2)
        self.bkp.measure_voltage(1)
        self.bkp.measure_voltage(2)

        self.meascur1_ent.configure(state=Tk.NORMAL)
        self.meascur1_ent.delete(0, len(self.meascur1_ent.get()))
        self.meascur1_ent.insert(0, str(self.bkp.currentMeasured1))
        self.meascur1_ent.configure(state='readonly')

        self.meascur2_ent.configure(state=Tk.NORMAL)
        self.meascur2_ent.delete(0, len(self.meascur2_ent.get()))
        self.meascur2_ent.insert(0, str(self.bkp.currentMeasured2))
        self.meascur2_ent.configure(state='readonly')

        self.measvol1_ent.configure(state=Tk.NORMAL)
        self.measvol1_ent.delete(0, len(self.measvol1_ent.get()))
        self.measvol1_ent.insert(0, str(self.bkp.voltageMeasured1))
        self.measvol1_ent.configure(state='readonly')

        self.measvol2_ent.configure(state=Tk.NORMAL)
        self.measvol2_ent.delete(0, len(self.measvol2_ent.get()))
        self.measvol2_ent.insert(0, str(self.bkp.voltageMeasured2))
        self.measvol2_ent.configure(state='readonly')

        self.parent.after(self.update_time_ms, self.update_measurements)

    def onoff1(self):
        """
command function for radio button ch1
        """
        if self.var1.get() == 1:
            self.bkp.turn_channel_on(1)
        elif self.var1.get() == 2:
            self.bkp.turn_channel_off(1)

    def onoff2(self):
        """
command function for radio button ch2
        """
        if self.var2.get() == 1:
            self.bkp.turn_channel_on(2)
        elif self.var2.get() == 2:
            self.bkp.turn_channel_off(2)

    def center_window(self):
        w = self.screenwidth / 1.5
        h = self.screenheight / 1.8
        x = (self.screenwidth - w) / 2
        y = (self.screenheight - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


# noinspection PyUnusedLocal
def main():
    HOSTIP = "142.103.235.210"
    bkp = Bkp.BKPRECISION9173(HOSTIP)
    root = Tk.Tk()
    app = GUI(root, bkp)
    app.update_measurements()
    root.mainloop()


if __name__ == '__main__':
    main()
