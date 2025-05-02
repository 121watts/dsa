# https://leetcode.com/problems/combination-sum-iii/

"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

"""

def combine(k: int, n: int):
    curr_comb, combs = [], []

    def backtrack(i, curr_comb, combs, n, k):
        if len(curr_comb) == k and sum(curr_comb) == n:
            combs.append(curr_comb.copy())
            return
        if i > 9:
            return

        for j in range(i, 9 + 1):
            curr_comb.append(j)
            backtrack(j + 1, curr_comb, combs, n, k)
            curr_comb.pop()

        # backtrack(i + 1, curr_comb, combs, n, k)

    backtrack(1, curr_comb, combs, n, k)

    return combs


print(combine(2, 4))
print(combine(9, 45))
