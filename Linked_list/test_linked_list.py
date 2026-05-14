from Linked_list_utils import LinkedList

# Example 1: Create a linked list and add elements
print("=== Example 1: Creating and Adding Elements ===")
ll = LinkedList()

# Create the first node
ll.create(10)
print("After creating with value 10:")
ll.display()

# Append elements at the end
ll.append(20)
print("After appending 20:")
ll.display()

ll.append(30)
print("After appending 30:")
ll.display()

ll.append(40)
print("After appending 40:")
ll.display()

print(f"Size: {ll.get_size()}\n")

# Example 2: Prepend elements at the beginning
print("=== Example 2: Prepending Elements ===")
ll.prepend(5)
print("After prepending 5:")
ll.display()

ll.prepend(1)
print("After prepending 1:")
ll.display()

print(f"Size: {ll.get_size()}\n")

# Example 3: Insert at specific index
print("=== Example 3: Inserting at Specific Index ===")
ll.insert_at(3, 15)
print("After inserting 15 at index 3:")
ll.display()

ll.insert_at(0, 0)
print("After inserting 0 at index 0:")
ll.display()

print(f"Size: {ll.get_size()}\n")

# Example 4: Convert to list
print("=== Example 4: Convert to Python List ===")
print(f"Linked List as Python list: {ll.to_list()}\n")

# Example 5: Create another linked list
print("=== Example 5: Create Another Linked List ===")
ll2 = LinkedList()
ll2.create(100)
ll2.append(200)
ll2.append(300)
print("Second linked list:")
ll2.display()
print(f"Size: {ll2.get_size()}")

