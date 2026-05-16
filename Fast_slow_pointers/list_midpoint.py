from Linked_list.Linked_list_utils import LinkedList


def find_midpoint(l1):
    slow = fast = l1.head
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    # Create a simple linked list with a cycle
    print("=== Creating a Linked List ===\n")
    l1 = LinkedList()
    for _ in range(12):
        l1.append(_)
    l1.display()
    print(find_midpoint(l1).val)
