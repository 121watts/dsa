# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the
# second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
# Your algorithm should use only constant space the input LinkedList should be modified in-place.

class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

# find middle of list
# return middle of list
# iterate over head and middle
# alternate h0 m0 h1 m1 and so on in place
# return head

class Solution():
    def rearrage(self, head):
        mid = self.get_mid(head)
        mid = self.reverse(mid)

        prev_head = None

        while head is not None and mid is not None:
            tmp = head.next
            head.next = mid
            head = tmp

            tmp = mid.next
            mid.next = head

        return prev

    def reverse(self, head):
        prev = None

        while head is not None:
            # store so it doesn't get overwritten
            next = head.next

            # overwrite next value
            head.next = prev

            # move iteration forward
            prev = head
            head = next

        return prev


    def get_mid(self, head):
        fast, slow = head, head

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(Solution().rearrage(head))
