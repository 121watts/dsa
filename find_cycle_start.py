# fast and slow pointer
# once fast == slow pointer we have found the cycle

class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

def find_cycle_start(head):
    fast, slow = head, head

    while True:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next.next

print(find_cycle_start(head).val)
