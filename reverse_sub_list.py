class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

class Solution:
  def reverse(self, head, p, q):
    # TODO: Write your code here
    return head



sol = Solution()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(sol.reverse(head, 2, 4))
