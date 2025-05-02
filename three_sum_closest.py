from math import inf
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# non-decreasing order which means there are duplicates that we need to skip
# okay, this is another 3sum problem
# difference here is we need to keep track of which sum is the closest to the target number
# we can store the closest_sum in a variable initializing it to infinity
# then we can keep track of the min(abs(target - current_closest, target - curr_sum))
# we can do this by tracking the abs(target - curr_sum)

def closet_sum_fn(arr, target_sum):
    arr.sort()
    closest_sum = inf

    for i in range(len(arr) - 1):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            x, y, z = arr[i], arr[left], arr[right]
            curr_sum = x + y + z

            print('x + y + z = curr_sum', x, y, z, curr_sum)
            print('closest_sum', closest_sum)

            if (curr_sum < 0 and target_sum >= 0) or (curr_sum > 0 and target_sum <= 0):
                curr_delta = abs(curr_sum + target_sum)
            else:
                curr_delta = abs(curr_sum - target_sum)

            if (closest_sum < 0 and target_sum > 0) or (closest_sum > 0 and target_sum < 0):
                closest_delta = abs(closest_sum + target_sum)
            else:
                closest_delta = abs(target_sum - closest_sum)

            if curr_delta < closest_delta:
                closest_sum = min(curr_sum, closest_sum)
                left += 1
            elif curr_delta > closest_delta:
                right -= 1
            else:
                left += 1
                right -= 1


    return closest_sum

# print(closet_sum_fn([-1, 0, 2, 3], 3))
print(closet_sum_fn([-3, -1, 1, 2], 1))
