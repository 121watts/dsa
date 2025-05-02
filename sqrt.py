# we can iterate over each integer from n -> x
# the very first time we get to n * n > x we know that n - 1 is the floor of the square root

def square_root(x: int) -> int:
    if x == 1:
        return 1

    for n in range(1, x + 1):
        print('current int: ', n)
        prod = n * n
        if prod > x:
            return n - 1


print(square_root(8))
print(square_root(2))
