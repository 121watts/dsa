
# two pointers
# left and right
# check to see if they sum to target
# if sum is less than target we need a bigger number so increment left
# if sum is > target we need a smaller number so decrement right
# if sum is == target return [left + 1, right + 1]
def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        left_n = numbers[left]
        right_n = numbers[right]

        sum = left_n + right_n

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]


print(twoSum([3,24,50,79,88,150,345], 200))
