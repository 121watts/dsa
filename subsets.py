from typing import List

# https://leetcode.com/problems/subsets/

def subsets(self, nums: List[int]) -> List[List[int]]:
    currSet, subsets = [], []

    def backtracker(index, currSet, subsets):
        if index == len(nums):
            subsets.append(currSet.copy())
            return

        # branch of decision tree that includes nums[index]
        currSet.append(nums[index])
        backtracker(index + 1, currSet, subsets)
        currSet.pop()

        # branch of decision tree that excludes nums[index]
        backtracker(index + 1, currSet, subsets)

    backtracker(0, currSet, subsets)

    return subsets




print(subsets(subsets, [1, 2, 3]))
