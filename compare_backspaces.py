class Solution:
    def compare(self, str1, str2):
        str1 = self.backspace(str1)
        str2 = self.backspace(str2)

        print(str1, str2)
        return str1 == str2

    def backspace(self, s):
        new_str = ""
        right = len(s) - 1
        bs_count = 0

        while right >= 0:
            char = s[right]
            # iterate from end of str to front
            # if not on a backspace prepend string onto new string new_str = char += new_str
            # if on backspace increment counter and dont preprend
            # if on char and bs_count > 0 dont prepend, decrement counter
            if char == "#":
                bs_count += 1
            elif bs_count > 0:
                bs_count -= 1
            else:
                new_str = char + new_str

            right -= 1

        return new_str

sol = Solution()

print(sol.compare("xy#z", "xzz#"))
print(sol.compare("xywrrp", "xywrrmu##p"))
