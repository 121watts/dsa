# two pointers
# increment / decrement each pointer until they reach an alphabetical char
# once they reach an alphabetical char compare.  if not equal, return false if equal continue the loop

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        left_str = s[left]
        right_str = s[right]

        if not left_str.isalnum():
            left += 1
            continue

        if not right_str.isalnum():
            right -= 1
            continue

        if left_str.lower() != right_str.lower():
            return False

        left += 1
        right -= 1

    return True



print(is_palindrome("A man, a plan, a canal, Panama!"))
print(is_palindrome('abc123'))
