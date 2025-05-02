#  https://uplevel.interviewkickstart.com/resource/rc-codingproblem-955846-1841905-2558-14354

def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    currSet, subsets = [], []

    def backtrack(index, currSet, subsets):
        if index == len(s):
            subsets.append("".join(currSet))
            return

        # start decision tree including s[i]
        currSet.append(s[index])
        backtrack(index + 1, currSet, subsets)
        currSet.pop()

        # start decision tree excluding s[i]
        backtrack(index + 1, currSet, subsets)

    backtrack(0, currSet, subsets)

    return subsets


print(generate_all_subsets("aac"))
