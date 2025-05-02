class Solution:
    def isValid(self, s: str) -> bool:

        closed_to_open = {
            '}': '{',
            ']': '[',
            ')': '(',
        }

        open = ['{', '[', '(']

        stack = []

        for char in s:
            if char in open:
                stack.append(char)
            else:
                closed_paren = char
                top_of_stack = stack[-1]
                if closed_to_open[closed_paren] != top_of_stack:
                    return False
                stack.pop()

        return True



sol = Solution()

print(sol.isValid("[]"))
print(sol.isValid("([{}])"))
print(sol.isValid("[(])"))
print(sol.isValid("["))
