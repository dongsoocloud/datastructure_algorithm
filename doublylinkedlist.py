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
        return True

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
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev_node = self.get(index-1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = current.prev
            prev_node.next = None
            current.prev = None
            self.tail = prev_node
        self.length -= 1
        return current
            
    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            next_node = current.next
            next_node.prev = None
            current.next = None
            self.head = next_node
        self.length -= 1
        return current
    
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        target = self.get(index)
        prev_node = target.prev
        next_node = target.next
        prev_node.next = next_node
        next_node.prev = prev_node
        target.next = None
        target.prev = None
        self.length -= 1
        return target





dll = DoublyLinkedList()
dll.append(3)
dll.append(5)
dll.append(7)
dll.append(9)
dll.pop()
dll.pop_first()
dll.print_list()
