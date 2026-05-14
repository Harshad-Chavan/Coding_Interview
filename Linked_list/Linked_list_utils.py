class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def create(self, val):
        """Create a new linked list with a single node"""
        new_node = ListNode(val)
        self.head = new_node
        self.tail = new_node
        self.size = 1
        return self

    def append(self, val):
        """Add an element at the end of the linked list"""
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return self

    def prepend(self, val):
        """Add an element at the beginning of the linked list"""
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return self

    def insert_at(self, index, val):
        """Insert an element at a specific index"""
        if index < 0 or index > self.size:
            print("Index out of bounds")
            return self

        if index == 0:
            return self.prepend(val)
        if index == self.size:
            return self.append(val)

        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return self

    def display(self):
        """Print the linked list"""
        if self.head is None:
            print("Linked List is empty")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def get_size(self):
        """Return the size of the linked list"""
        return self.size

    def to_list(self):
        """Convert linked list to a Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
