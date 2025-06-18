class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ''

        for order_char in order:
            for s_char in s:
                if order_char == s_char:
                    result =  result + s_char

        for s_char in s:
            if s_char not in order:
                result += s_char

        return result


sol = Solution()

print(sol.customSortString('cba', 'abcad'))
