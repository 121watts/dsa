class Node:
    def __init__(self, key, value):
        self.prev, self.next = None, None
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.cache = {}

        # left = LRU  right = MRU
        self.left.next = self.right
        self.right.prev = self.left

    # insert node at right most position
    def insert(self, node):
        next, prev = self.right, self.right.prev

        # put the new node inbetween the old mru and right dummy
        next.prev = node
        prev.next = node

        # point the new MRU next to right dummy
        node.next = next
        # point the new MRU prev to the old mru
        node.prev = prev


    # remove from list
    def remove(self, node):
        new_next = node.next
        new_prev = node.prev

        new_prev.next = new_next
        new_next.prev = new_prev


    def get(self, key: int) -> int:
        # we need to make this the most recently used
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove LRU from the list and the cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


lru = LRUCache(2)
lru.put(1, 10)  # cache {[1]: pointer to node with value 10}
print(lru.get(1))     # return value of 10
lru.put(2, 20)  # cache: {[1]: ptr to 10, [2]: ptr to 20 }
lru.put(3, 30)  # cache: {[2]: ptr 20, [3]: ptr to 30}
lru.get(2)      # return 20 (2 is not most recently used)
print(lru.get(1))     # return -1 node of key 1 is no longer in the cache
