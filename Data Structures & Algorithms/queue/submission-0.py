class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Works like a pointer to the next node
        self.prev = None  # Works like a pointer to the previous node

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        newNode = Node(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popValue = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return popValue

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popValue = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return popValue