# https://neetcode.io/problems/combinations-of-a-phone-number
'''
Letter Combinations of a Phone Number
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

What would "33" output to?
are ef and fe equivalent? # no, because 3 is pressed first and then 4.
So, we want each branch where d is included and def are excluded

https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/796a0dc1-2fcd-4ebb-0686-28f9007ec800/public
'''

def combine(digits: str):
    phone_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    curr_combs, combinations = [], []

    def backtrack(digit_index, curr_combs, combinations):
        if len(curr_combs) == len(digits):
            combinations.append("".join(curr_combs))
            return


        char = digits[digit_index]
        letters = phone_letters[char]

        for letter in letters:
            curr_combs.append(letter)
            backtrack(digit_index + 1, curr_combs, combinations)
            curr_combs.pop()


    backtrack(0, curr_combs, combinations)

    return combinations

print(combine('345'))
