def get_distinct_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """

    s = "".join(sorted(s))
    currSet, subsets = [], []

    def backtrack(index, currSet, subsets):
        if index == len(s):
            subsets.append(currSet.copy())
            return

        currSet.append(s[index])
        backtrack(index + 1, currSet, subsets)
        currSet.pop()

        while index < len(s) - 1 and s[index] == s[index + 1]:
            index += 1

        backtrack(index + 1, currSet, subsets)


    backtrack(0, currSet, subsets)

    return subsets

print(get_distinct_subsets("aab"))
