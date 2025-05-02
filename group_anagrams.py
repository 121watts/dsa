from typing import List

# iterate over list
# sort each element
# check if in dict {[str]: arr}
# if in dict append original string to arr
# put all values in dict into new array

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = {}

    for str in strs:
        sorted_str = "".join(sorted(str))

        if sorted_str in anagrams:
            anagrams[sorted_str].append(str)
        else:
            anagrams[sorted_str] = [str]

    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
