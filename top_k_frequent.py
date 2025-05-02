# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List

# initiallize and array of size n
# the index is the frequency
# the value is an array with numbers at that frequency (index)
# iterate backwards over the array
# keep a counter of size k
# each element we hit that isnt empty add those values to output array
# decerement counter by len(arr_of_values_at_index_frequency)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[]] * len(nums)
