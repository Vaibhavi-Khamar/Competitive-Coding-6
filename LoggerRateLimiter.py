# # doubly Linked list and hashmap
# # Tc: O(1) for all operations
# # Sc: O(n) for storing messages in the hashmap
# class Node:
#     def __init__(self, timestamp: int, message: str):
#         self.timestamp = timestamp
#         self.message = message
#         self.prev = None
#         self.next = None

# class Logger:
#     MAX_TIME = 10

#     def __init__(self):
#         self.map = {}  # message -> Node
#         self.head = Node(0, "")  # dummy head
#         self.tail = Node(0, "")  # dummy tail
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message in self.map:
#             node = self.map[message]
#             if timestamp - node.timestamp < self.MAX_TIME:
#                 return False
#             self._moveToHead(node, timestamp)
#         else:
#             if len(self.map) >= self.MAX_TIME:
#                 self._removeTail()
#             self._addToHead(timestamp, message)
#         return True

#     def _addToHead(self, timestamp: int, message: str):
#         new_node = Node(timestamp, message)
#         new_node.next = self.head.next
#         new_node.prev = self.head
#         self.head.next.prev = new_node
#         self.head.next = new_node
#         self.map[message] = new_node

#     def _removeTail(self):
#         node_to_remove = self.tail.prev
#         node_to_remove.prev.next = self.tail
#         self.tail.prev = node_to_remove.prev
#         self.map.pop(node_to_remove.message)

#     def _moveToHead(self, node: Node, timestamp: int):
#         node.timestamp = timestamp
#         # Disconnect from current position
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         # Move to head
#         node.next = self.head.next
#         node.prev = self.head
#         self.head.next.prev = node
#         self.head.next = node


# Doubly linedlist & hashmap
class Logger:
    class Node:
        def __init__(self, message: str, timestamp: int):
            self.message = message
            self.timestamp = timestamp
            self.prev = None
            self.next = None
    def __init__(self):
        self.map = {}  # message -> Node
        self.interval = 10
        self.head = self.Node("", -1)  # dummy head
        self.tail = self.Node("", -1)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.map:
            node = self.map[message]
            if timestamp - node.timestamp < self.interval:
                return False  # too soon
            node.timestamp = timestamp
            self._removeNode(node)
            self._addToHead(node)
        else:
            new_node = self.Node(message, timestamp)
            self.map[message] = new_node
            self._addToHead(new_node)
        return True
    def _addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# # Hashmap
# class Logger:
#     def __init__(self):
#         self.msg_time = {}  # message -> last printed timestamp
#     def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
#         if message not in self.msg_time:
#             self.msg_time[message] = timestamp
#             return True
#         if timestamp - self.msg_time[message] >= 10:
#             self.msg_time[message] = timestamp
#             return True
#         return False