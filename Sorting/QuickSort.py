def Partition(arr, start, end):
    pivot = arr[end]
    pos = start

    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1

    arr[pos], arr[end] = arr[end], arr[pos]

    return pos


def QuickSort(arr, start, end):
    if start >= end:
        return

    pivot = Partition(arr, start, end)

    print("Pivot:", pivot, "Value:", arr[pivot])

    QuickSort(arr, start, pivot - 1)
    QuickSort(arr, pivot + 1, end)


arr = [3, 5, 8, 2, 9, 1, 4]

QuickSort(arr, 0, len(arr) - 1)

print(arr)