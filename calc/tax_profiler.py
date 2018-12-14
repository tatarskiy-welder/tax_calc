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

    def get_revenue(self):
        return self.__revenue

    def set_pfr(self):
        self.__pfr = float(self.PFR) / 4

        if self.__revenue >= self.PFR_LIMIT:
            self.__pfr += (self.__revenue - self.PFR_LIMIT) * self.PFR_PROCENT

    def get_pfr(self):
        return self.__pfr

    def set_oms(self):
        self.__oms = float(self.OMS) / 4

    def get_oms(self):
        return self.__oms

    def set_usn(self):
        self.__usn = self.get_revenue() * self.USN_PROCENT - \
            self.get_pfr() - self.get_oms()

        if self.__usn < 0:
            self.__usn = 0

    def set_revenue(self, revenue):
        if revenue <= 0:
            revenue = 0
        else:
            self.__revenue = revenue

        self.set_pfr()
        self.set_oms()
        self.set_usn()

    def get_usn(self):
        return round(self.__usn, 2)
