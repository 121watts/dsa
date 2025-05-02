# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# traverse linked list
# track prev node
# if curr node val == val prev.next == curr.next
# move pointers forward prev == curr

class Solution:
    def removeElements(self, head, val):
        prev, curr = None, head

        while curr:
            if curr.val == val:
                prev.next = curr.next

            curr = curr.next

        return prev

sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)


print(sol.removeElements(head, 6).__dict__)
