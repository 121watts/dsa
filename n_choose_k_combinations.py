def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """

    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    # Write your code here.
    return result


print(find_combinations(5, 2))
