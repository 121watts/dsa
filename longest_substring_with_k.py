def find_length(str1, k):
    max_len = 0
    left = 0
    distinct_k = set()

    for right in range(len(str1)):
        distinct_k.add(str1[right])
        if len(distinct_k) <= k:
            max_len = max(max_len, right - left + 1)

        while len(distinct_k) > k:
            print(distinct_k, left, right)
            distinct_k.discard(str1[left])
            left += 1

    return max_len

print(find_length("araaci", 1))
