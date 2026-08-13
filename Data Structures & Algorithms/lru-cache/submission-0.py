class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:

        # existing update
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node) 
        else:
            # new node
            ## with capacity
            if len(self.map) == self.capacity:
                lastNode = self.tail.prev
                self.removeNode(lastNode)
                del self.map[lastNode.key]
            newNode = self.Node(key, value)
            self.addToHead(newNode) 
            self.map[key] = newNode

        
