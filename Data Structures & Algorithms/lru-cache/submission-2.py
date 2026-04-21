class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.caches = {}
        self.head = None
        self.tail = None
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        if prev:
            prev.next = nxt
        else:
            self.head = nxt
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        node.prev = node.next = None
        return node
        
    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def get(self, key: int) -> int:
        if key in self.caches:
            node = self.caches[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            self.caches[key].val = value
            self.remove(self.caches[key])
            self.insert(self.caches[key])
        else:
            node = Node(key, value)
            self.caches[key] = node
            self.insert(node)
        
        if len(self.caches) > self.cap:
            self.caches.pop(self.head.key)
            self.remove(self.head)
        
