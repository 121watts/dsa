class Solution:
    def valid_palindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        num_del = 1

        while end > start:
            s1 = s[start]
            s2 = s[end]

            if s1 != s2:
                num_del -= 1
                if num_del >= 0:
                    end -= 1
                else:
                    return False
            elif s1 == s2:
                start += 1
                end -= 1

        return True




sol = Solution()

print(sol.valid_palindrome('a'))
print(sol.valid_palindrome('aba'))
print(sol.valid_palindrome('abca'))
print(sol.valid_palindrome('abcca'))
print(sol.valid_palindrome('deeee'))
