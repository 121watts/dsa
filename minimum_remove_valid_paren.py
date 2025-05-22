# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

# my intuition here is to maintain a stack of parens
# construct a sequence of valid parens
# iterate over the string
# if its a letter append it to the result string
# if we hit a paren attempt to match it with the corresponding paren in the paren stack
# if its a match append it to result string and increment the paren stack index

class Solution:
    def min_remove(self, s: str) -> str:
        open = []
        closed = []
        result = ""

        for char in s:
            if char == "(":
                open.append(char)
            elif char == ")" and len(open) > len(closed):
                closed.append(")")

        open = []

        for _ in closed:
            open.append("(")

        print(open, closed)

        for char in s:
            if char == "(" and len(open):
                result += open.pop()
            elif char == ")" and len(closed) > len(open):
                result += closed.pop()
            elif char.isalpha():
                result += char

        return result


sol = Solution()

print(sol.min_remove("le)e)t(co)de"))
