class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
        self.length = 0
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index > self.length / 2:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        else:
            current = self.head
            for _ in range(index):
                current = current.next
        return current
    
    def set_value(self, index, value) -> bool:
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False
    
    def insert(self, index, value) -> bool:
        pass
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
            current.prev = None
        self.length -= 1
        return current
            
    def pop_first(self) -> Node:
        pass

    



dll = DoublyLinkedList()
dll.append(3)
dll.append(5)
dll.append(7)
dll.append(9)
dll.pop()
dll.print_list()
