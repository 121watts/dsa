def search_triplets(arr, target):
    counter = 0
    arr.sort() # nlogn
    print(arr)

    for i in range(len(arr) - 1):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            x, y, z = arr[i], arr[left], arr[right]
            sum = x + y + z
            print(f'{x} + {y} + {z} = {sum}')

            if sum < target:
                counter += right - left
                left += 1
            else:
                right -= 1

    return counter

# print(search_triplets([-1, 0, 2, 3], 3))
# expected: 2

print(search_triplets([-1, 4, 2, 1, 3], 5))
# after sort [-1, 1, 2, 3, 4]
# expected: 4
