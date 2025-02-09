def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))

target = 23
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(f"Target found at index: {binary_search(arr,target)}")