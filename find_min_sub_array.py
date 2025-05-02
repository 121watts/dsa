def find_min(target, arr):
    left = 0
    min_len = len(arr) + 1
    curr_sum = 0

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1

    if min_len > len(arr):
        min_len = 0

    return min_len

print(find_min(7, [2, 1, 5, 2, 3, 2]))
