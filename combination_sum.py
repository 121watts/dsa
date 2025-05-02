# https://leetcode.com/problems/combination-sum/
# TODO

def combination_sum(candidates, target):
    curr_comb, combs = [], []

    def backtrack(i, curr_comb, combs):
        summed = sum(curr_comb)
        if sum(curr_comb) == target:
            combs.append(curr_comb.copy())
            return
        if summed > target:
            return

        for i in range(len(candidates)):
            curr_comb.append(candidates[i])
            backtrack(i + 1, curr_comb, combs)
            curr_comb.pop()

            # backtrack(i + 1, curr_comb, combs)

    backtrack(1, curr_comb, combs)

    return combs

print(combination_sum([2,3,5], 8))
