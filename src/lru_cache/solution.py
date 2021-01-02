class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:
    def __init__(self, capacity: int):
        self.max_size = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        """ Returns the value for a given cache key """
        node = self.cache.get(key, None)

        # cache miss
        if not node:
            return -1

        # cache hit node most recently used
        if node == self.head:
            return node.val

        # pop node from list
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt

        # if node is tail update new tail
        if node == self.tail:
            self.tail = node.prev
        # node is not tail so update prev
        else:
            nxt.prev = prev

        # replace head as node is now most recently accessed
        tmp = self.head
        self.head = node
        self.head.nxt = tmp
        self.head.prev = None
        tmp.prev = self.head

        return node.val

    def put(self, key: int, val: int) -> None:
        if self.cache.get(key):
            node = self.cache.get(key)
            node.val = val
            self.get(key)
            return
        node = Node(key, val)
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        if node and node.val != val:
            node.val = val

        if len(self.cache) >= self.max_size:
            # pop tail
            del self.cache[self.tail.key]
            self.tail = self.tail.prev
            self.tail.nxt = None

        # move node to head to indicate recently used
        tmp = self.head
        self.head = node
        self.head.nxt = tmp
        tmp.prev = self.head
        self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
