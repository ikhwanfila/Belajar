class UangBulanan(object):
    def __init__ (self,Uang):
        self.Uang = Uang
    def Influx(self,Pemasukan):
        self.Uang = self.Uang + Pemasukan
    def Emission(self,Pengeluaran):
        self.Uang = self.Uang - Pengeluaran
    def Status(self):
        print("Uang :",self.Uang)

def main():
    Ikhwan = UangBulanan(1000000)
    Ikhwan.Status()
    Ikhwan.Influx(500000)
    Ikhwan.Status()
    Ikhwan.Emission(250000)
    Ikhwan.Status()

if __name__ == '__main__':
    main()