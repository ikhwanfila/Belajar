def Penjumlahan(N):
    for i in range(N):
        A,B = map(int,input("Masukan 2 bilangan: ").split())
        print("Hasil Penjumlahan: ",A+B)

def main():
    N = int(input("Masukan Angka: "))
    Penjumlahan(N)

if __name__ == '__main__':
    main()