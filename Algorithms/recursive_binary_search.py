def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr)//2

        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
                return recursive_binary_search(arr[midpoint+1:], target)
            else:
                return recursive_binary_search(arr[:midpoint], target)


def check(result):
    print(f"Target found: {result}")


arr = [_ for _ in range(1, 10)]
target = 7
result = recursive_binary_search(arr, target)
check(result)
