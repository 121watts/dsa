# two pointers left and right
# since the array is sorted and the squares of negative numbers are positive
# we can keep track of which index to use
# we find the largest square by comparing the left and right pointers
# the largest square goes into the current highest index
# if left pointer larger increment
# if right pointer larger decrement

def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]

    left = 0
    right = n - 1
    highest_square_index = n - 1

    while left < right:
        left_n = arr[left]
        right_n = arr[right]

        left_sq = left_n * left_n
        right_sq = right_n * right_n

        if left_sq > right_sq:
            squares[highest_square_index] = left_sq
            left += 1
            highest_square_index -= 1
        elif right_sq > left_sq:
            squares[highest_square_index] = right_sq
            right -= 1
            highest_square_index -= 1
        else:
            squares[highest_square_index] = left_sq
            highest_square_index -= 1
            left += 1

            squares[highest_square_index] = right_sq
            highest_square_index -= 1
            right -= 1

    return squares

print(make_squares([-2, -1, 0, 2, 3]))
