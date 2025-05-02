from typing import AnyStr

def check_pangram(sentence: AnyStr):
    LEN_ALPHA = 26
    sentence_set = set()
    sentence = sentence.lower()

    for char in sentence:
        if char.isalpha():
            sentence_set.add(char)

    return LEN_ALPHA == len(sentence_set)


print(check_pangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
