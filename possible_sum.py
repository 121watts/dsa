def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """

    curr_set, combinations = [], []

    def backtrack(index, curr_set, combinations):
        if len(curr_set) > 0 and sum(curr_set) == k:
            combinations.append(curr_set.copy())
            return
        if index == len(arr):
            return

        curr_set.append(arr[index])
        backtrack(index + 1, curr_set, combinations)
        curr_set.pop()

        backtrack(index + 1, curr_set, combinations)

    backtrack(0, curr_set, combinations)
    sum_is_possible = len(combinations) != 0
    # Write your code here.
    return sum_is_possible


print(check_if_sum_possible([2, 4, 8], 6))
print(check_if_sum_possible([2, 2, 2], 6))
print(check_if_sum_possible([1], 0))
