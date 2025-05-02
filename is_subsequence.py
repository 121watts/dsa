# if we find s_char == t_char increment s_idx
# if s_idx + 1 == len(s) we have found a solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_idx = 0
        t_idx = 0
        seq = []

        while t_idx < len(t):
            s_char = s[s_idx]
            t_char = t[t_idx]

            if s_char == t_char:
                seq.append(s_char)
                s_idx += 1

            if s_idx == len(s):
                return True

            t_idx += 1


        return False


sol = Solution()

print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("abx", "ahbgdc"))
