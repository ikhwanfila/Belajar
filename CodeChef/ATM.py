def ATM(A,B):
    if B > A:
        if A % 5 == 0:
            print("Sisa Saldo =",B-A-0.5)
        else:
            print("Saldo =",B)
    else:
        print("Saldo Tidak Cukup =",B)

def main():
    Biaya = float(input("Masukan Jumlah yang akan diambil: "))
    Saldo = float(input("Masukan Saldo : "))
    ATM(Biaya,Saldo)
    
if __name__ == '__main__':
    main()