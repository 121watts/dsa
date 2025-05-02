class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

def has_cycle(head: Node) -> bool:
    slow, fast = head, head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

n1 = Node(1)
head = Node(0)
head.next = n1
head.next.next = Node(2)
head.next.next.next = Node(3)

no_cycle = head
print(has_cycle(no_cycle))

head.next.next.next = n1
print(has_cycle(head))
