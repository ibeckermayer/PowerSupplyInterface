"""
Code modified largely from: http://zetcode.com/gui/tkinter/
"""

import Tkinter as tk


class UI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.master.title("Power Supply Interface")  # master gives access to the root window (Tk)
        self.pack(fill=tk.BOTH, expand=1)  # put our Frame on entire Tk window
        self.centerWindow()

    def centerWindow(self):
        w = self.master.winfo_screenwidth()/1.1
        h = self.master.winfo_screenheight()/1.3

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = tk.Tk()
    app = UI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
