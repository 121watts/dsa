# split number into digits
# for each digit square and sum
# if square and sum == 1 return True
# if square and sum in set return False
# otherwise keep splitting

def find(num, s=None) -> bool:
    if s is None:
        s = set()
    if num == 1:
        return True
    if num in s:
        return False

    digits = [int(d) for d in str(num)]

    s.add(num)

    new_num = 0

    for d in digits:
        new_num += d * d

    return find(new_num, s)

print(find(23))
print(find(1))
print(find(12))
