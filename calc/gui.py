from tkinter import *
from tax_profiler import TaxProfile
from tkinter import messagebox as mb


class Example(Frame, TaxProfile):
    def __init__(self, parent):
        TaxProfile.__init__(self)
        Frame.__init__(self, parent, background="lightblue")
        parent.minsize(width=500, height=200)
        parent.maxsize(width=500, height=200)
        self.parent = parent
        self.initUI()

    def get_those_numbers(self, event):
        try:
            self.set_revenue_last(int(self.entry1.get()))
            self.set_usn_paid(int(self.entry2.get()))
            self.set_oms_paid(int(self.entry3.get()))
            self.set_pfr_paid(int(self.entry4.get()))
        except ValueError:
            mb.showerror("Error", "Введите все данные числами")
            return
        self.top.destroy()

    def kvartal_windows(self):
        try:
            self.kvartal = int(self.entry_kvartal.get())
        except ValueError:
            mb.showerror("Error", "Введите квартал числом (1-4)")
        if self.kvartal < 1 or self.kvartal > 4:
            mb.showerror("Error", "Введите квартал числом (1-4)")
            return
        self.top_start.destroy()

        if self.kvartal == 1:
            return

        self.top = Toplevel(width=650, height=250)
        self.top.minsize(200, 400)
        self.top.title("Начало работы")
        label1 = Message(
            self.top, text="Данные за предыдущие кварталы", bg="lightblue", bd=5,
            relief="groove", font=("Helvetica", 12))
        label1.pack()

        label2 = Message(self.top, text="Введите доход:", bg="lightblue", bd=5,
                         relief="groove", font=("Helvetica", 12))
        label2.pack()
        self.entry1 = Entry(self.top)
        self.entry1.pack()

        label3 = Message(self.top, text="Введите УСН:", bg="lightblue", bd=5,
                         relief="groove", font=("Helvetica", 11))
        label3.pack()
        self.entry2 = Entry(self.top)
        self.entry2.pack()

        label4 = Message(self.top, text="Введите ПФР:", bg="lightblue", bd=5,
                         relief="groove", font=("Helvetica", 11))
        label4.pack()
        self.entry3 = Entry(self.top)
        self.entry3.pack()

        label5 = Message(self.top, text="Введите ФФОМС:", bg="lightblue", bd=5,
                         relief="groove", font=("Helvetica", 11))
        label5.pack()
        self.entry4 = Entry(self.top)
        self.entry4.pack()

        button = Button(self.top, text="Далее")
        button.pack()
        button.bind("<Button-1>", self.get_those_numbers)

    def start_window(self):

        self.top_start = Toplevel()
        self.top_start.title("Начало работы")
        self.top_start.minsize(150, 100)
        self.top_start.maxsize(150, 100)

        msg = Message(self.top_start, text="Введите текущий квартал")
        msg.pack()
        self.entry_kvartal = Entry(self.top_start)
        self.entry_kvartal.pack()

        button = Button(
            self.top_start, text="Далее",
            command=self.kvartal_windows)
        button.pack()

    def output(self, event):

        default = "0"
        self.entry_fond["text"] = default
        self.entry_pfr["text"] = default
        self.entry_usn["text"] = default
        try:
            self.set_revenue(int(self.entry_dohod.get()))
            if int(self.entry_dohod.get()) <= 0:
                mb.showerror("Error", "Введите число в графу доход")
            else:
                self.entry_fond["text"] = self.get_oms()
                self.entry_pfr["text"] = self.get_pfr()
                self.entry_usn["text"] = self.get_usn()
        except ValueError:
            mb.showerror("Error", "Введите число в графу доход")

    def initUI(self):
        self.parent.title("Калькулятор налогов")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(4, weight=2)
        dohod = Label(self, text="Доход:", bg="lightblue", bd=5,
                      relief="groove", font=("Helvetica", 12))

        dohod.grid(sticky=W, pady=4, padx=10, column=0, row=1)

        nalog = Label(self, text="Налоги:", bg="lightblue", bd=5,
                      relief="groove", font=("Helvetica", 12))

        nalog.grid(sticky=W, pady=10, padx=10, column=2, row=0)

        usn = Label(self, text="УСН:", bg="lightblue", bd=5,
                    relief="groove", font=("Helvetica", 12))

        usn.grid(sticky=W, pady=4, padx=10, column=2, row=1)

        pfr = Label(self, text="ПФР:", bg="lightblue", bd=5,
                    relief="groove", font=("Helvetica", 12))

        pfr.grid(sticky=W, pady=4, padx=10, column=2, row=2)

        fond = Label(self, text="ФФОМС:", bg="lightblue", bd=5,
                     relief="groove", font=("Helvetica", 12))

        fond.grid(sticky=W + N, pady=4, padx=10, column=2, row=3)

        self.entry_dohod = Entry(self)
        self.entry_dohod.grid(sticky=W, pady=4, padx=5, column=1, row=1)

        self.entry_usn = Label(self, text=self.get_usn(), bg="white", width=15)
        self.entry_usn.grid(sticky=W + N, pady=4, padx=5, column=3, row=1)

        self.entry_pfr = Label(self, text=self.get_pfr(), width=15, bg="white")
        self.entry_pfr.grid(sticky=W + N, pady=4, padx=5, column=3, row=2)

        self.entry_fond = Label(
            self, text=self.get_oms(), width=15, bg="white")
        self.entry_fond.grid(sticky=W + N, pady=4, padx=5, column=3, row=3)

        ras = Button(self, text="Рассчитать", width=30)
        ras.grid(row=3, column=0, columnspan=2, sticky=W + S + E + N, padx=10)

        self.start_window()

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
    root.iconbitmap(r'py.ico')
    app = Example(root)
    root.resizable(width=False, height=False)
    root.mainloop()


if __name__ == '__main__':
    main()
