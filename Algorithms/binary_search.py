def binary_search(arr, target):
    if len(arr) == 0:
        return
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last)//2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


arr = [10, 11, 12, 13, 24, 35, 46, 57, 68, 79]
target = 11
print(binary_search(arr, target))
