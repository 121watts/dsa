# array is sorted so we can have a left and right pointer
# if left + right < target increment left pointer
# if left + right > target decrement right pointer
# if equal we have found our target and return the two indices

def search(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum < target_sum:
            left += 1
        elif curr_sum > target_sum:
            right -= 1
        else:
            return [left, right]

    return [-1, -1]


print(search([1, 2, 3, 4, 6], 6))
