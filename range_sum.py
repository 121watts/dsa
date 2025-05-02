# https://leetcode.com/problems/range-sum-query-immutable/
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix()

    def prefix(self):
        tmp = [self.nums[0]]

        for i in range(1, len(self.nums)):
            prev_sum = tmp[i - 1]
            curr = self.nums[i]

            tmp.append(prev_sum + curr)

        self.prefix_sum = tmp


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]

na = NumArray([-2, 0, 3, -5, 2, -1])

print(na.nums)
print(na.prefix_sum)
print(na.sumRange(2, 5))
print(na.sumRange(0, 5))
