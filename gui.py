from tkinter import *
from tax_profiler import TaxProfile
from tkinter import messagebox as mb


class Example(Frame, TaxProfile):
    def __init__(self, parent):
        TaxProfile.__init__(self)
        Frame.__init__(self, parent, background="lightblue")
        self.parent = parent
        self.initUI()

    def output(self, event):
        try:
            self.set_revenue(int(self.entry_dohod.get()))
            self.entry_fond["text"] = self.get_oms()
            self.entry_pfr["text"] = self.get_pfr()
            self.entry_usn["text"] = self.get_usn()
        except ValueError:
            mb.showerror("Error", "Введите число в графу доход")

    def initUI(self):
        self.parent.title("Калькулятор налогов")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(5, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        dohod = Label(self, text="Доход:")
        dohod.grid(sticky=W + N, pady=4, padx=5, column=0, row=4)

        nalog = Label(self, text="Налоги:")
        nalog.grid(sticky=W + N, pady=4, padx=5, column=3, row=0)

        usn = Label(self, text="УСН:")
        usn.grid(sticky=W + N, pady=4, padx=5, column=3, row=1)

        pfr = Label(self, text="ПФР:")
        pfr.grid(sticky=W + N, pady=4, padx=5, column=3, row=2)

        fond = Label(self, text="ФФОМС:")
        fond.grid(sticky=W + N, pady=4, padx=5, column=3, row=3)

        self.entry_dohod = Entry(self)
        self.entry_dohod.grid(sticky=W + N, pady=4, padx=5, column=1, row=4)

        self.entry_usn = Label(self, text=self.get_usn(), bg="white", width=15)
        self.entry_usn.grid(sticky=W + N, pady=4, padx=5, column=4, row=1)

        self.entry_pfr = Label(self, text=self.get_pfr(), width=15, bg="white")
        self.entry_pfr.grid(sticky=W + N, pady=4, padx=5, column=4, row=2)

        self.entry_fond = Label(
            self, text=self.get_oms(), width=15, bg="white")
        self.entry_fond.grid(sticky=W + N, pady=4, padx=5, column=4, row=3)

        ras = Button(self, text="Рассчитать", width=30)
        ras.grid(row=4, column=2, sticky=W + S + N + E)

        ras.bind("<Button-1>", self.output)

        self.centerWindow()

    def centerWindow(self):
        w = 650
        h = 250

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
