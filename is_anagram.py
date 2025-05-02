from collections import defaultdict

def is_anagram(s: str, t: str):
    dict = defaultdict(int)

    for char in s:
        dict[char] += 1

    for char in t:
        dict[char] -= 1

    for key in dict:
        if dict[key] != 0:
            return False

    return True


print(is_anagram("listen", "silent"))
print(is_anagram("plerps", "serps"))
