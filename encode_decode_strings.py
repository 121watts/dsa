from typing import List

class Solution:
    def encode(self, strings: List[str]) -> str:
        s = ""
        for string in strings:
            s = s + f'{len(string)}#{string}'

        return s

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0

        while i < len(s):
            # Parse the length prefix
            length_str = ''
            while s[i] != '#':
                length_str += s[i]
                i += 1

            length = int(length_str)
            i += 1

            string = ''
            while length > 0:
                string += s[i]
                i += 1
                length -= 1

            strings.append(string)

        return strings


sol = Solution()

# print(sol.encode(["neet","01234567890123456789","love"]))
# Output: 4#neet4#code#love
# print(sol.decode("4#neet4#code4#love"))
