def PenjumlahanList(N): 
    for i in range(N):
        A = str(input("Masukan Bilangan :"))
        B = list(map(int,A))
        sum = 0
        for i in range(len(B)):
            sum = sum + B[i]
        print("Hasil Penjumlahan =",sum)
        
def main():
    N = int(input("Masukan Bilagan: "))
    PenjumlahanList(N)
    
if __name__ == '__main__':
    main()