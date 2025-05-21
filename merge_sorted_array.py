from typing import List

# modify nums1 in place
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1 # largest value in nums1's index
        p2 = n - 1 # largets value in nums2's index
        p3 = len(nums1) - 1

        while p3 > 0:
            l1 = nums1[p1]
            l2 = nums2[p2]

            if l1 > l2:
                nums1[p3] = l1
                p1 -= 1
                p3 -= 1
            elif l2 > l1:
                nums1[p3] = l2
                p2 -= 1
                p3 -= 1
            else:
                nums1[p3] = l1
                nums1[p3 - 1] = l2
                p1 -= 1
                p2 -= 1
                p3 -= 2




sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2, 5, 6], 3)
print(nums1)

nums1 = [1]
sol.merge(nums1, 1, [], 0)
print(nums1)

nums1 = [0]
sol.merge(nums1, 0, [1], 1)
print(nums1)
