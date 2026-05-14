from Linked_list_utils import *


def reverse_linked_list(l):
    prev_node = None
    curr_node = l.head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        # important step move both PV and CN forward
        prev_node = curr_node
        curr_node = next_node
    l1.head = prev_node


if __name__ == "__main__":
    l1 = LinkedList()
    l1.create(1)
    for i in range(2, 5):
        l1.append(i)

    l1.display()
    reverse_linked_list(l1)
    l1.display()
