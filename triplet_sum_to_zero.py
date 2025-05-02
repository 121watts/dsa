# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# Explanation: There are four unique triplets whose sum is equal to zero.

# if we sort the array first we can use a three sum approach to solving this problem.
# sorting is nlogn.
# x + y + z = 0
# we can iterate over each number which we will call x
# inside of that loop we can use two_sum technique w/ two pointers and search for each combination of numbers that when added together with x
# equal zero
# if the previous number is the same as the current number we skip that iteration as to avoid duplicates

def search_triplets(arr):
    result = []
    arr.sort()

    for i in range(len(arr) - 1):
        left = i + 1
        right = len(arr) - 1

        # avoid duplicate calculations
        if arr[i] == arr[i - 1] and i > 0:
            print('skipping index', i)
            continue

        while left < right:
            print('checking to see if i skipped index: ', i)
            x, y, z = arr[i], arr[left], arr[right]

            sum = x + y + z

            if right != len(arr) - 1:
                if arr[right] == arr[right + 1]:
                    right -= 1
                    continue

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else: # sum == 0
                left += 1
                right -= 1
                result.append([x, y, z])


    return result


# print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
# # Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# print(search_triplets([0,0,0]))
# # Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

print(search_triplets([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# Actual: [[-4, -2, 6], [-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, -2, 4], [-2, 0, 2]]
# Expected: [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
