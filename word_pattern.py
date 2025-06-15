from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        result = True
        words = s.split()
        map = defaultdict(str)

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            print(char, word)

            if char in map:
                if map[char] != word:
                    result = False

            map[char] = word


        return result


sol = Solution()
print(sol.wordPattern('abba', 'dog dog dog dog'))
