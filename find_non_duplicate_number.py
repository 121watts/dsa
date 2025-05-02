# initiate a count to 0
# if n != n + 1 increment counter
# otherwise just continue on the loop

def move_elements(arr):
    count = 0

    for i in range(len(arr)):
        n = arr[i]
        next_n = -1000

        if i < len(arr) - 1:
            next_n = arr[i + 1]

        if n != next_n:
            count += 1

    return count

print(move_elements([2, 3, 3, 3, 6, 9, 9]))
