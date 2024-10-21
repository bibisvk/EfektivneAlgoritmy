from MergeSort import MergeSort
from QuickSort import QuickSort

if __name__ == '__main__':
    A = [5, 7, 1, 3, 4, 6, 9, 2, 8]
    QuickSort(A, 0, len(A)-1)
    print(A)

    B = [5, 7, 1, 3, 4, 6, 9, 2, 8]
    MergeSort(B, 0, len(B)-1)
    print(B)
