class Node:
    def __init__(self, key, val):
        self.prev, self.next = None, None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.least, self.most = Node(0, 0), Node(0, 0)
        self.least.next = self.most
        self.most.prev = self.least


    # points its prev to its next
    # and then inserts itself at the tail
    def insert(self, node: Node):
        # this was the previously most recently used
        most_prev = self.most.prev
        most_prev.next = node
        node.prev = most_prev
        node.next = self.most
        self.most.prev = node

    # removes job is to simply take this node and remove its pointers to everything
    # and let garbage collection remove it from existence
    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # for getting a node we return the value at key
    # then we must also remove the pointers that node has currently
    # and move it to the tail of the linked list
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]

        self.remove(node)
        self.insert(node)

        return self.store[key]


    # for adding a node, we must add it to the store
    # if the key is already in the store, we must add it to the store AND
    # remove the previous node from the linked list and add this new node
    # to the end of the linked list
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])

        node = Node(key, value)
        self.store[key] = node
        self.insert(node)

        if len(self.store) > self.capacity:
            least = self.least.next
            del self.store[least.key]
            self.remove(self.least.next)



lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
lru.get(1)
lru.put(3, 3)

curr = lru.least
print(lru.store)

while curr:
    print(curr.key, curr.val)
    curr = curr.next
