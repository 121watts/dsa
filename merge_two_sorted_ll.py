# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1

        c1 = list1
        c2 = list2

        while c1 or c2:
            v1 = None
            v2 = None

            if c1:
                v1 = c1.val

            if c2:
                v2 = c2.val

            if v1 is not None and v2 is not None:
                if v1 > v2:
                    tmp = c2
                    c2.next = c1
                    c2 = tmp.next
                    c1 = c1.next
