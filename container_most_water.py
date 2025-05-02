# https://neetcode.io/problems/max-water-container
from math import inf


def maxArea(heights):
    max_area = 0
    i = 0
    j = len(heights) - 1

    while i < j:
        left_h = heights[i]
        right_h = heights[j]

        length = j - i
        height = min(left_h, right_h)

        curr_area = length * height

        max_area = max(max_area, curr_area)

        if left_h < right_h:
            i += 1
        else:
            j -= 1

    return max_area


print(maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
print(maxArea([2, 2, 2]))
