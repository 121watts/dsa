from typing import List

# we don't care about zero values but we do care about positioning
# they are the same length so we can iterate over them at the same time
# it tells me to store the sparse vectors "efficiently" so i dont know what that means
# the naive way is to just return the lists on init iterate over them ignore calculation for zero values
# non-naive way we can use a tuple to store values and indices in the list
# iterate over the shorter of the two lists
# if the indices match then multiple them together and add to the dot_product

class SparseVector:
    def __init__(self, nums: List[int]):
        # vector_val = (index, value)
        vec = []
        for i in range(len(nums)):
            n = nums[i]
            if n > 0:
                vec.append((i, n))

        print(vec)
        self.vec_vals = vec

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0

        for i in range(len(vec.vec_vals)):
            (i1, v1) = vec.vec_vals[i]
            (i2, v2) = self.vec_vals[i]

            if i1 != i2:
                continue

            dot_product += v1 * v2

        return dot_product




# Your SparseVector object will be instantiated and called as such:
nums1 = [0,0,0,0,0,0,3,0,0,3,0,0,0]
nums2 = [0,0,2,0,0,4,3,0,0,2,0,0,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)

print(ans)
