"""
Code modified largely from: http://zetcode.com/gui/tkinter/
"""

import Tkinter as tk


class UI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.screenwidth = self.parent.winfo_screenwidth()
        self.screenheight = self.parent.winfo_screenheight()
        self.relativePadx = self.screenwidth/384.
        self.relativePady = self.screenheight/240.

        self.parent.title("Power Supply Interface")  # master gives access to the root window (Tk)
        self.pack(fill=tk.BOTH, expand=1)  # put our Frame on entire Tk window
        self.centerWindow()

        self.UIwidth = self.winfo_width()
        self.UIheight = self.winfo_height()

        self.initUI()

    def initUI(self):
        self.createLabelFrame()

    def createLabelFrame(self):
        # Create the main frame for the label
        labelFrame = tk.Frame(self, borderwidth=self.relativePadx*.5, relief=tk.GROOVE)
        labelFrame.pack(side=tk.TOP, fill=tk.X, padx=self.relativePadx, pady=self.relativePady)
        # Create "POWER SUPPLY:"
        ps_lab = tk.Label(labelFrame, text="POWER SUPPLY:")
        ps_lab.pack(side=tk.LEFT, padx=self.relativePadx * 5)
        ps_lab.config(font=("Arial", 22))
        # Create name of the power supply
        name_lab = tk.Label(labelFrame, text="BK PRECISION 9173")
        name_lab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        name_lab.config(font=("Arial", 22))

        # Create separate frame for the IP ADDRESS label and entry box
        ipFrame = tk.Frame(labelFrame)
        ipFrame.pack(side=tk.RIGHT, pady=self.relativePady*2)
        ip_lab = tk.Label(ipFrame, text="IP ADDRESS")
        ip_lab.pack(side=tk.TOP) #, anchor=tk.E, padx=self.relativePadx*5)
        ip_lab.config(font=("Arial", 22))
        ip = tk.Entry(ipFrame)
        ip.insert(0, "142.103.235.210")
        ip.configure(state='readonly', font=("Arial", 14), justify="center")
        ip.pack(side=tk.BOTTOM, anchor=tk.E, padx=self.relativePadx*5)

    def centerWindow(self):
        w = self.screenwidth / 1.1
        h = self.screenheight / 1.3
        x = (self.screenwidth - w) / 2
        y = (self.screenheight - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = tk.Tk()
    app = UI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
