def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range (p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, j, i)
    exchange(A, r, i+1)
    return i+1

def exchange(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]  # Swapping elements at indexes x and y
    return arr
