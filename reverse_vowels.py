# create a constant of vowels to compare against
# iterate over string from back to front and collect them in new string
# iterate over master string, append each char to new string
# if char is a vowel, consult reversed list
def reverse_vowels(s: str) -> str:
    vowels = 'aeiouAEIOU'
    reversed_vowels = []
    curr_vowel_idx = 0
    result = ''

    for char in s:
        if char in vowels:
            reversed_vowels.append(char)

    reversed_vowels.reverse()

    for char in s:
        if char in vowels:
            result += reversed_vowels[curr_vowel_idx]
            curr_vowel_idx += 1
        else:
            result = result + char

    return result

print(reverse_vowels("DesignGUrus"))
