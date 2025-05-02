# get each string recursively
# iterate over each character backtrack over each of the chars in this string
# reverse the capitalization of each of these if they are alphabetical
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """

    result, curr_str = [], []

    def backtrack(index, curr_str):
        if len(curr_str) == len(s):
            curr = "".join(curr_str)
            if curr not in result:
                result.append(curr)
            return

        curr_str.append(s[index])
        backtrack(index + 1, curr_str)
        curr_str.pop()

        if s[index].isalpha:
            curr_str.append(s[index].swapcase())
            backtrack(index + 1, curr_str)
            curr_str.pop()

    backtrack(0, curr_str)


    return result


print(letter_case_permutations("a1z"))
