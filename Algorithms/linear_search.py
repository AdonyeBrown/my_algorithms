def linear_search(arr, target):
    if len(arr) == 0:
        return

    for i in range(len(arr)):
        if arr[i] == target:
            return i


def check(result):
    print(f"Target found at index: {result}")


arr = [_ for _ in range(1, 10)]
target = 7
result = linear_search(arr, target)
check(result)
