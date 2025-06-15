from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            print(slow.val)
            print(fast.val)

            if slow == fast:
                return True

        return False




head = ListNode(1)
cycle_next = ListNode(2)
head.next = cycle_next
head.next.next = ListNode(0)
cycle = ListNode(4).next = cycle_next
head.next.next.next = ListNode(4)

sol = Solution()
print(sol.hasCycle(head))
