from typing import List

def letter_case_permutations(s: str) -> List[str]:
    # Write your code here.
    result = []

    def backtrack(index, path):
        if index == len(s):
            result.append("".join(path))
            return

        path.append(s[index])
        backtrack(index + 1, path)
        path.pop()

        if s[index].isalpha():
            path.append(s[index].swapcase())
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(letter_case_permutations("a1z"))
