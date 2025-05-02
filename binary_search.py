def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left < right:
        mid = (right + left) // 2

        print(left, right, mid)
        if target == arr[mid]:
            return mid
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] > target:
            right = mid - 1

    return result


print(binary_search([-1, 0, 1, 2, 3, 4, 6, 8], 4))
