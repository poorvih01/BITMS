def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1, 3, 5, 2, 87, 74, 69]
bubble_sort(arr)
print("Sorted array is:", arr)
