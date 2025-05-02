# binary search over each row
# if target in between first and last element of row
# binary search over that row
def search_matrix(matrix, target):
    left, right = 0, len(matrix) - 1

    while left <= right:
        mid = (left + right) // 2
        left_row = matrix[left]
        right_row = matrix[right]
        mid_row = matrix[mid]

        if target > mid_row[len(left_row) - 1]:
            left = mid + 1
        elif target < mid_row[0]:
            right = mid - 1
        else:
            return binary_search(mid_row, target)
            # binary search over mid


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        print(arr, left, mid, right)
        if arr[mid] < target:
            print('left')
            left = mid + 1
        elif arr[mid] > target:
            print('right')
            right = mid - 1
        else:
            print('found bin search')
            return True

    return False


matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10

print(search_matrix(matrix, target))
