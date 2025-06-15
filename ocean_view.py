from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        len_heights = len(heights)

        tallest_idx = len_heights - 1
        next_idx = tallest_idx - 1
        result.append(tallest_idx)

        while next_idx >= 0:
            tallest_val = heights[tallest_idx]
            next_val = heights[next_idx]

            if next_val > tallest_val:
                tallest_idx = next_idx
                result.append(next_idx)

            next_idx -= 1

        result.reverse()
        # print(result)
        return result

sol = Solution()
sol.findBuildings([4, 2, 3, 1])
sol.findBuildings([4, 3, 2, 1])
sol.findBuildings([1, 3, 2, 4])
sol.findBuildings([4, 4, 4, 4])
