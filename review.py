class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
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
    
    def get(self, index):
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
    
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value) -> bool:
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
    
    def insert(self, index, value) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev_node = self.get(index - 1)
        next_node = prev_node.next
        next_node.prev = new_node
        new_node.next = next_node
        new_node.prev = prev_node
        prev_node.next = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        last_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev_node = last_node.prev
            prev_node.next = None
            last_node.prev = None
            self.tail = prev_node
        self.length -= 1
        return last_node 
    
    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        first_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            next_node = first_node.next
            next_node.prev = None
            first_node.next = None
            self.head = next_node
        self.length -= 1
        return first_node
    
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev_node = self.get(index - 1)
        target_node = prev_node.next
        next_node = target_node.next
        next_node.prev = prev_node
        prev_node.next = next_node
        target_node.next = None
        target_node.prev = None
        self.length -= 1
        return target_node

dd = DoubleLinkedList(1)
dd.append(2)
dd.append(3)
dd.append(4)
dd.append(5)
dd.append(6)
dd.append(7)
dd.append(8)
dd.append(9)
dd.append(10)
dd.print_list()
dd.insert(2, 7)
dd.print_list()


    