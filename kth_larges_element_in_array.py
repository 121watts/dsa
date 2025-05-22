# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
import heapq

class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        max_heap = []
        result = None
        heapq.heapify(max_heap)

        for n in nums:
            heapq.heappush(max_heap, -n)

        for _ in range(k):
            result = -heapq.heappop(max_heap)

        print(result)

        return result



sol = Solution()

sol.find_kth_largest([3,2,1,5,6,4], 2)
