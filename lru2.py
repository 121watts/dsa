class Node:
    def __init__(self, key: int, value: int):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store: Dict[int, Node] = {}
        self.least = Node(0, 0)
        self.most = Node(0, 0)
        self.least.next, self.most.prev = self.most, self.least


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        self.remove(self.store[key])
        self.insert(key)

        return self.store[key].value

    # 1. change most prev pointer to new node
    # 2. create pointers for new node
    #   2a. new node.next to most
    #   2b. new node.prev to most's prev node
    # 3. change next pointer of the previously most recent node
    def insert(self, key: int) -> None:
        node = self.store[key]

        most_prev = self.most.prev
        most_prev.next = node
        self.most.prev = node
        node.prev = most_prev
        node.next = self.most

    def remove(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    # when we add a value to the LRUCache we need to:
    # 1. add the value
    # 2. insert it at most
    # 3. check to see if we are above capacity
    # 4. remove the node after least
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            old_node = self.store[key]
            self.remove(old_node)

        self.store[key] = Node(key, value)
        self.insert(key)

        if len(self.store) > self.capacity:
            node_to_remove = self.least.next
            self.remove(node_to_remove)
            del self.store[node_to_remove.key]

        return None
