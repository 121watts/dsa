
# list is no sorted
# we can use hashmap to store values and their indices
def two_sum(numbers, target):
  """
  Args:
   numbers(list_int32)
   target(int32)
  Returns:
   list_int32
  """
  seen = {}

  for index, n in enumerate(numbers):
    delta = target - n

    if delta in seen:
      return [seen[delta], index]

    seen[n] = index

  return [-1, -1]

print(two_sum([4, 1, 5, 0, -1], 10))
print(two_sum([4, 1, 6, 0, -1], 10))
