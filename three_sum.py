from typing import List


# remember to skip duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            x = nums[i]

            while left < right:
                y, z = nums[left], nums[right]
                total = x + y + z

                if total == target:
                    result.append([x, y, z])
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result



sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([0, 0, 0]))
