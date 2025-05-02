# we range from k -> 1 where 1 is i
# where the swapping takes place from -i and (-i + k)

def rotate(nums, k):
    left = nums[:k+1] # give me all the values before k+1
    right = nums[k+1:] # give me all the values after k+1
    nums[:k+1] = right
    nums[k:] = left

rotate([1,2,3,4,5,6,7], 3)
