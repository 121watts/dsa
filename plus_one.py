from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_len = len(digits) - 1
        i = list_len
        nine_found = False

        while i >= 0:
            n = digits[i]

            if n == 9 and i == list_len:
                nine_found = True
                digits[i] = 0
            elif n == 9 and nine_found:
                digits[i] = 0
            elif nine_found:
                nine_found = False
                digits[i] = n + 1
            elif i == list_len:
                digits[i] = n + 1


            i -= 1

        if nine_found:
            return [1] + digits

        return digits

sol = Solution()

print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([9]))
print(sol.plusOne([1, 0, 9]))
print(sol.plusOne([1, 0, 9]))
print(sol.plusOne([1, 1, 1, 1, 1, 1, 1]))
print(sol.plusOne([9, 9, 8, 9, 9, 9]))
