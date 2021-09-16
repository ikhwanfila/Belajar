def JumlahBarisan(a,b,Un):
    A = [int]*Un
    for i in range(Un):
        A[i] = a + (b*i)
    print("List =",A)
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]
    print("Jumlah semua List = ",sum)

def main():
    a = int(input("Masukan Bilangan Pertama = "))
    b = int(input("Masukan Beda = "))
    Un = int(input("Masukan Banyak data = "))
    JumlahBarisan(a,b,Un)

if __name__ == '__main__':
    main()