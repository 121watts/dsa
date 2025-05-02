from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    nums_set = set(nums)

    return len(nums) == len(nums_set)


print(contains_duplicate([1, 2, 3, 1]))
