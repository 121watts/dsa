from typing import List
from math import inf

# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            is_start_of_sequence = n - 1 not in num_set

            if is_start_of_sequence:
                length = 1

                while (n + length) in num_set:
                    length += 1

                longest = max(longest, length)

        return longest




sol = Solution()

print(sol.longestConsecutive([100,4,200,1,3,2]))
