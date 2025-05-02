def sort(arr):
    left = 0
    mid = 0
    right = len(arr) - 1

    while mid <= right:
        print(left, right, mid)
        right_val = arr[right]
        mid_val = arr[mid]
        left_val = arr[left]

        print(right_val, mid_val, left_val)

        if mid_val == 0:
            arr[left] = mid_val
            arr[mid] = left_val
            left += 1
            mid += 1
        elif mid_val == 2:
            arr[mid] = right_val
            arr[right] = mid_val
            right -= 1
        else: # mid_val is where its supposed to be
            mid += 1

    return arr

print(sort([2, 2, 0, 1, 2, 0]))
# print(sort([1, 0, 2, 1, 0]))
