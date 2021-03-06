class TaxProfile():
    """docstring for TaxProfile """

    PFR = 26545
    OMS = 5840
    USN_PROCENT = 0.06
    PFR_LIMIT = 300000
    PFR_PROCENT = 0.01

    def __init__(self):
        self.__revenue = 0
        self.__pfr = 0
        self.__oms = 0
        self.__usn = 0
        self.__revenue_last = 0
        self.__pfr_paid = 0
        self.__oms_paid = 0
        self.__usn_paid = 0
        self.kvartal = 0

    def get_revenue_last(self):
        return self.__revenue_last

    def get_usn_paid(self):
        return self.__usn_paid

    def get_pfr_paid(self):
        return self.__pfr_paid

    def get_oms_paid(self):
        return self.__oms_paid

    def set_revenue_last(self, revenue):
        self.__revenue_last = revenue

    def set_pfr_paid(self, pfr):
        self.__pfr_paid = pfr

    def set_oms_paid(self, oms):
        self.__oms_paid = oms

    def set_usn_paid(self, usn):
        self.__usn_paid = usn

    def get_revenue(self):
        return self.__revenue

    def set_pfr(self):
        if self.__revenue >= self.PFR_LIMIT:
            self.__pfr = (self.__revenue - self.PFR_LIMIT) * \
                self.PFR_PROCENT + self.PFR
        else:
            self.__pfr = self.PFR

        self.__pfr = float(self.__pfr - self.__pfr_paid) / (5 - self.kvartal)
        if self.__pfr < 0:
            self.__pfr = 0

    def get_pfr(self):
        return round(self.__pfr, 2)

    def set_oms(self):
        self.__oms = (float(self.OMS) - self.__oms_paid) / (5 - self.kvartal)
        if self.__oms < 0:
            self.__oms = 0

    def get_oms(self):
        return round(self.__oms, 2)

    def set_usn(self):
        self.__usn = self.get_revenue() * self.USN_PROCENT - \
            self.get_pfr() - self.get_oms() - self.get_usn_paid()

        if self.__usn < 0:
            self.__usn = 0

    def set_revenue(self, revenue):
        self.__revenue = revenue + self.get_revenue_last()

        self.set_pfr()
        self.set_oms()
        self.set_usn()

    def get_usn(self):
        return round(self.__usn, 2)
