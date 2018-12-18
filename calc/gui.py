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

    def getThoseNumbers(self):
                self.__revenue_last = self.entry1.get()
                self.__pfr_paid = self.entry2.get()
                self.__oms_paid = self.entry3.get()
                self.__usn_paid = self.entry4.get()
                self.top.destroy()

    def kvartal_windows(self):

        self.__kvartal = int(self.entry_kvartal.get())

        self.top_start.destroy()

        if self.__kvartal == 1:
            return

        try:
            self.top = Toplevel()
            self.top.title("Начало работы")
            label1 = Message(
                self.top, text="Данные за предыдущие кварталы")
            label1.pack()

            label2 = Message(self.top, text="Введите доход:")
            label2.pack()
            self.entry1 = Entry(self.top)
            self.entry1.pack()

            label3 = Message(self.top, text="Введите УСН:")
            label3.pack()
            self.entry2 = Entry(self.top)
            self.entry2.pack()

            label4 = Message(self.top, text="Введите ПФР:")
            label4.pack()
            self.entry3 = Entry(self.top)
            self.entry3.pack()

            label5 = Message(self.top, text="Введите ФФОМС:")
            label5.pack()
            self.entry4 = Entry(self.top)
            self.entry4.pack()

            button = Button(self.top, text="Дальше",
                            command=self.getThoseNumbers)
            button.pack()

        except ValueError:
            mb.showerror("Error", "Введите число в графу доход")

    def start_window(self):
        def closing(self):
            self.top_start.destroy()

        self.top_start = Toplevel()
        self.top_start.title("Начало работы")

        msg = Message(self.top_start, text="Введите текущий квартал")
        msg.pack()
        self.entry_kvartal = Entry(self.top_start)
        self.entry_kvartal.pack()

        button = Button(
            self.top_start, text="С учетом предыдущих кварталов",
            command=self.kvartal_windows)
        button.pack()

    def output(self, event):
        # top = Toplevel()
        # top.title("About this application...")

        # msg = Message(top, text="Some testing stuff, nothing to do here")
        # msg.pack()

        # button = Button(top, text="Dismiss", command=top.destroy)
        # button.pack()

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
