class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = x // 2
        is_calculating = True

        while is_calculating:
            square = sqrt * sqrt

            if square == x:
                return sqrt
            elif square > x:
                return sqrt - 1
            else:
                sqrt += 1


sol = Solution()
print(sol.mySqrt(1))
print(sol.mySqrt(2))
print(sol.mySqrt(8))
print(sol.mySqrt(9))
print(sol.mySqrt(121))
