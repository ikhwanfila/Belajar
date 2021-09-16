def TesInput(A,B):
    sum = 0
    for i in range(A):
        O = int(input("Masukan angka: "))
        if O % B == 0:
            sum = sum + 1
    print(sum)

def main():
    N = int(input("Masukan berapa banyak angka: "))
    M = int(input("Masukan angka yang jadi pembagi: "))
    TesInput(N,M)
    
if __name__ == '__main__':
    main()