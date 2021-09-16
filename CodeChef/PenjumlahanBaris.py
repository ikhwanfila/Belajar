def Penjumlahan(a):
    for i in range(a):
        b = int(input("Masukan angka: "))
        sum = 0
        j = 0
        for j in range(b):
            sum = sum + j + 1
        print("Hasil =",sum)

def main():
    a = int(input("Masukan Perulangan: "))
    Penjumlahan(a)
    
if __name__ == '__main__':
    main()