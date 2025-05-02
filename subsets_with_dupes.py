from typing import List
# https://leetcode.com/problems/subsets-ii/

# we are gonna use backtracking here
# the backtracking will help us form
# the two branches of the decision trees
# those that include the nums[i] and those that exclude nums[i]
# for duplicates, on the branch that excludes nums[i] we will
# first sort the array so we can
# skip over each element that is equal to the next element

def subsets_with_dupes(nums: List[int]):
    nums = sorted(nums)
    curr_set, subsets = [], []

    def backtrack(index, curr_set, subsets):
        if index == len(nums):
            subsets.append(curr_set.copy())
            return

        # branch that includes
        curr_set.append(nums[index])
        backtrack(index + 1, curr_set, subsets)
        curr_set.pop()

        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1

        # branch that excludes
        backtrack(index + 1, curr_set, subsets)


    backtrack(0, curr_set, subsets)

    return subsets


print(subsets_with_dupes([1, 2, 2, 3]))
print(subsets_with_dupes([1, 1, 1, 1]))
print(subsets_with_dupes([4, 4, 4, 1, 4]))
