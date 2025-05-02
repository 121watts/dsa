# this is 3 sum with another loop
# w, x, y, z = target

def search_quads(arr, target):
    result = []
    arr.sort()

    for i in range(len(arr) - 1):
        # avoid duplicate values
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 1):
            # avoid duplicate values
            if j > i + i and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = len(arr) - 1

            while left < right:
                w, x, y, z = arr[i], arr[j], arr[left], arr[right]
                sum = w + x + y + z
                print(f'{w} + {x} + {y} + {z} = {sum}')

                if sum == target:
                    result.append([w, x, y, z])
                    left += 1
                    right -= 1
                elif sum > target:
                    right -= 1
                else: # sum < target
                    left += 1

    return result

print(search_quads([0,0,0,0], 0))
