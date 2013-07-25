#!/usr/bin/python
"""GUI application to generate Pi to specified decimal places"""


from tkinter import *

from pi_lib import pi


class Pypi(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        self.grid()
        label_input = Label(self, anchor="w", text="Number of Digits:")
        label_input.grid(column=0, row=0, columnspan=1, sticky='EW')

        self.no_of_digits = StringVar()
        self.e_input = Entry(self, textvariable=self.no_of_digits)
        self.e_input.grid(column=1, row=0, sticky='EW')
        self.e_input.bind("<Return>", self.compute)
        self.no_of_digits.set("5")

        b_compute = Button(self, text="Compute pi !", command=self.compute)
        b_compute.grid(column=2, row=0)

        l_pi = Label(self, anchor="w", text=" Value of Pi")
        l_pi.grid(column=0, row=1, sticky='EW')

        self.t_answer = Text(self, width=8, height=1)
        self.t_answer.grid(column=1, row=1, sticky='EW')
        self.t_answer.insert('1.0', "3.14159")

        b_clip = Button(self, text="Copy to Clipboard", command=self.copy_clip)
        b_clip.grid(column=2, row=1)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

    def compute(self, event=None):
        """computes pi and changes textbox"""
        digits = self.no_of_digits.get()
        self.t_answer.delete('1.0', END)
        self.t_answer.insert('1.0', (pi(int(digits))))

    def copy_clip(self):
        """Copy to clipboard"""
        self.clipboard_clear()
        self.clipboard_append(self.t_answer.get('1.0', 'end'))

if __name__ == "__main__":
    app = Pypi(None)
    app.title('Find Pi')
    app.mainloop()
