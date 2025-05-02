# https://leetcode.com/problems/combinations/
from typing import List

# combinations are VERY similar to setting up subsets.  but instead of ALL subsets we are
# asking for a range of subsets of a particular size.  and since we only want some of a particular
# size we don't need to go down the branch of "not selected" like we do in subsets.
# we can simply iterate through 1 - n and backtrack

def combine(n: int, k: int) -> List[List[int]]:
    comb, combs = [], []

    def backtrack(i, comb, combs, n, k):
        if len(comb) == k:
            combs.append(comb.copy())
            return
        if i > n:
            return

        # we iterate 1 -> n but each recursive call i increments
        # so we in effect remove the appends for the next number
        for j in range (i, n + 1):
            comb.append(j)
            backtrack(j + 1, comb, combs, n, k)
            comb.pop()

    backtrack(1, comb, combs, n, k)

    return combs

print(combine(4, 2))
