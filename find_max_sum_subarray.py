from math import inf

# sliding window technique here
# store previous sum in variable
# subtract prev element that just left the window
# add new element that just entered the window
# use curr_max = max(curr_max, curr_sum)
# im going to assume that k is always less than the size of the array

def findMaxSumSubArray(k, arr):
  # calculate first sum
  curr_sum = 0

  for i in range(k):
    curr_sum += arr[i]

  curr_max = curr_sum

  for i in range(len(arr) - k):
    window_end = i + k
    curr_sum += arr[window_end] - arr[i]
    curr_max = max(curr_sum, curr_max)

  return curr_max

print(findMaxSumSubArray(3, [2,1,5,1,3,2]))
print(findMaxSumSubArray(2, [2, 3, 4, 1, 5]))
print(findMaxSumSubArray(1, [1, 2, 3, 4, 5]))
