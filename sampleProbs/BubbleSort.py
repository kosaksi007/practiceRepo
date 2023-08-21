def bubbleSort(arr: list):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


# bubbleSort([2,1,5,6,3,9,0])
def selectionSort(arr: list):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(arr)


# selectionSort([2,1,5,6,3,9,0])


def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0:
            if val < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = val
                j -= 1
            else:
                break
    print(arr)


# insertionSort([2,1,5,6,3,9,0])
def insertionSorting(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0:
            if val < arr[j]:
                arr[j + 1] = arr[j]
                arr[j] = val
                j -= 1
            else:
                break
    print(arr)
insertionSorting([2,1,5,6,3,9,0])