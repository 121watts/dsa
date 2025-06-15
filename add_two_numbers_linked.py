from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        curr_1 = l1
        curr_2 = l2
        carry = 0

        while curr_1 or curr_2:
            # edge case for either curr being null
            n1 = 0
            n2 = 0

            if curr_1:
                n1 = curr_1.val
                curr_1 = curr_1.next

            if curr_2:
                n2 = curr_2.val
                curr_2 = curr_2.next

            val = 0

            if n1 + n2 + carry > 10:
                val = (n1 + n2 + carry) - 10
                carry = 1
            elif n1 + n2 + carry == 10:
                val = 0
                carry = 1
            else:
                val = n1 + n2 + carry
                carry = 0

            dummy.next = ListNode(val)
            dummy = dummy.next


        if carry:
            dummy.next = ListNode(1)

        curr = head
        while curr:
            print(curr.val)
            curr = curr.next



        return head.next


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(3)
# l2.next = ListNode(4)
# l2.next.next = ListNode(5)

sol = Solution()
sol.addTwoNumbers(l1, l2)
