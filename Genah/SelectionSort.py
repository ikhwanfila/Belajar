def SelectionSort(A):
    n = len(A)
    i = 0
    while i != n:
        for j in range(i+1,n):
            print("i =",i,"j =",j)
            print("A[i] =",A[i],"A[j] =",A[j])
            if A[i]>A[j]:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
            print(A)
            print("")
        i = i+1
    print("Data yang sudah terurut =",A)

def main():
    L = [11,334,523,12,12]
    SelectionSort(L)

if __name__ == '__main__':
    main()