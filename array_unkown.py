def search(reader, target):
    oob = 2**31 - 1
    left = 0
    right = 10**4

    while left <= right:
        mid = (left + right) // 2
        mid_val = reader.get(mid)

        if mid_val == target:
            return mid
        elif mid_val == oob:
            mid = right // 2
            right = 10**4 - 1
        elif mid_val > target:
            left = mid + 1
        elif mid_val < target: # mid_val < target
            right = mid - 1


    return -1




search('foo', 'bar')
