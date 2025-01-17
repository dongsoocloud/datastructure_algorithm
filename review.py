class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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

    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
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
    
    def prepend(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
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
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            prev_node = self.head
            while current.next:
                prev_node = current
                current = current.next
            prev_node.next = None
            self.tail = prev_node
        self.length -= 1
        return current
    
    def pop_first(self) -> Node:
        if self.length == 0:
            return Node
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            current.next = None
        self.length -= 1
        return current
            
    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        target_node = prev_node.next
        prev_node.next = target_node.next
        target_node.next = None
        self.length -= 1
        return target_node

ll = LinkedList()
ll.prepend(1)
ll.append(2)
ll.prepend(0)
ll.append(3)
ll.append(4)

ll.set_value(2, 6)
ll.print_list()

ll.remove(2)
ll.print_list()