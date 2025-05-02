from collections import defaultdict

def put_in_baskets(fruits):
    max_len = 0
    basket = defaultdict(int)
    left = 0

    for right in range(len(fruits)):
        right_fruit = fruits[right]
        basket[right_fruit] += 1

        print(left, right, basket)

        while len(basket) > 2:
            left_fruit = fruits[left]

            if basket[left_fruit] > 1:
                basket[left_fruit] -= 1
            else:
                basket.pop(left_fruit)

            left += 1

        max_len = max(max_len, sum(basket.values()))

    return max_len

print(put_in_baskets(['A', 'B', 'C', 'A', 'C']))
print(put_in_baskets(['A', 'A', 'A', 'A', 'A']))
print(put_in_baskets(["A", "A", "A", "B", "C", "C", "C"]))
