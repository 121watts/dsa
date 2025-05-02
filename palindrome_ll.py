class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

# first we want to find the middle node.
# once we've found the middle node, we want to reverse the second half of the list
# once we have reversed the list we want to then go back from the middle and compare the start to the middle for each node
# of there's a node with a diff val its not a palindrome
class Solution:
    def isPalindrome(self, head):
        mid = self.find_mid(head)
        reversed_head = self.reverse(mid)

        curr = head
        curr_reversed = reversed_head

        while curr_reversed:
            if curr.val != curr_reversed.val:
                return False

            curr_reversed = curr_reversed.next
            curr = curr.next

        return True

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next # store swapped node for later so we dont overwrite it
            curr.next = prev # reverse the link
            prev = curr # move prev forward
            curr = next # set curr forward

        return prev

    def find_mid(self, head):
        fast, slow = head, head

        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow



head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
# head.next.next.next.next = Node(2)

sol = Solution()
print(sol.isPalindrome(head))
