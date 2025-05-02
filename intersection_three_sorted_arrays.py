# iterate through the shortest list
# we want three pointers each starting at the first index
# if pointers at all three indices are equal
# add values to the list and increment all pointers
# we want to move the value of the smallest number forward
def find_intersection(arr1, arr2, arr3):
  """
  Args:
   arr1(list_int32)
   arr2(list_int32)
   arr3(list_int32)
  Returns:
   list_int32
  """
  result = []

  i, j, k = 0, 0, 0  # Three pointers for each array

  while i < len(arr1) and j < len(arr2) and k < len(arr3):
      # If all elements are equal, add to result
      if arr1[i] == arr2[j] == arr3[k]:
          result.append(arr1[i])
          i += 1
          j += 1
          k += 1
      # Move the pointer of the smallest value forward
      elif arr1[i] < arr2[j]:
          i += 1
      elif arr2[j] < arr3[k]:
          j += 1
      else:
          k += 1

  return result if result else [-1]  # Return [-1] if no intersection


print(find_intersection(
[1, 1, 2, 2],
[1, 2, 2, 2, 9],
[1, 1, 1, 2, 2, 2]
))
