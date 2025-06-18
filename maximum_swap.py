from math import inf

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = f'{num}'
        highest = -inf
        nums = []

        for char in num_str:
            n = int(char)
            nums.append(n)
            if n > highest:
                highest = n

        for i in range(len(nums)):
            n = nums[i]

            if n == highest:
                first_n = nums[0]
                nums[0] = str(n)
                nums[i] = str(first_n)
            else:
                nums[i] = str(n)

        return int(''.join(nums))

sol = Solution()

print(sol.maximumSwap(2736))
print(sol.maximumSwap(9973))
print(sol.maximumSwap(1039))
