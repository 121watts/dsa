# okay we have the store in a dict so we can get O(1) gets
# we need the linked list so we can get O(1) puts and removals
# whenever there's any operation on a node other than delete
# it needs to move to the tail of the list
# edge cases:
# -

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.least, self.most = Node('least', 'least'), Node('most', 'most')
        self.least.next = self.most
        self.most.prev = self.least


    def remove_ptrs(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def print_list(self):
        curr = self.least
        s = 'LinkedList => '
        ctr = 0
        while curr:
            s += f'Node_{ctr} key={curr.key} val={curr.val} -> '
            ctr += 1
            curr = curr.next

        print(s)

    # create link to most and new node
    # remove link from most.prev and most.prev.next
    def insert(self, node: Node):
        node.next = self.most
        node.prev = self.most.prev
        self.most.prev.next  = node
        self.most.prev = node

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]

        self.remove_ptrs(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        print('putting key, val', key, value)

        if key in self.store:
            self.remove_ptrs(self.store[key])

        node = Node(key, value)
        self.store[key] = node
        self.insert(node)

        if len(self.store) > self.capacity:
            print('at capacity')
            least_next = self.least.next

            self.print_list()
            print(self.store)
            del self.store[least_next.key]
            self.remove_ptrs(least_next)








# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(1)

obj.put(1, 'remove_me')
obj.put(2, 2)
obj.put(3, 3)
obj.put(1, 'keep_me')
