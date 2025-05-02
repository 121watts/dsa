def sort(nums):
    i = 0

    while i < len(nums):
        value_should_be = i + 1
        curr_value = nums[i]

        if curr_value != value_should_be:
            nums[i] = value_should_be
            swap_index = curr_value - 1
            nums[swap_index] = curr_value

        i += 1

    return nums


print(sort([3, 1, 5, 4, 2]))
