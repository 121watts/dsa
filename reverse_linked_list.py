# i want to swap head and next
# in order to do that next needs to be the new head
# next.next needs to be the previous head
# head.next needs to be what was next.next.next
# move curr forward

class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next


class Solution:
  def reverse(self, head):
    prev, curr = None, head

    while curr:
        tmp = curr.next
        curr.next = prev # reversing pointer e.g. null -> 4 -> 8 -> 10 to null <- 4 (no pointer here now, we will do that next iteration of loop) 8 -> 10
        prev = curr # move prev pointer up e.g. moving from {prev} null <- 4 8 to null <- {prev} 4 8
        curr = tmp # move curr pointer up e.g. null <- {curr} 4 8 -> 10 to  null <- {prev} 4 {curr} 8 -> 10 (note that the next iteration will link 4 to 8 (4 <- 8))

    return prev

sol = Solution()
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)


result = sol.reverse(head)
print(result.__dict__)
print(result.next.__dict__)
