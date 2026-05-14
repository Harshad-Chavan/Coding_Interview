from Linked_list_utils import *


def find_intersection_node(l1, l2):
    ptr_l1 = l1.head
    ptr_l2 = l2.head

    while ptr_l1 != ptr_l2:

        # basically start with l1 and when you reach the end start with l2
        # as for both the lists the tail nodes will be the same
        ptr_l1 = ptr_l1.next if ptr_l1 else l2.head
        ptr_l2 = ptr_l2.next if ptr_l2 else l1.head

    print(ptr_l1.val)
    return ptr_l1


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()

    l1.append(1)
    l1.append(3)
    l1.append(4)

    l2.append(6)
    l2.append(4)

    l3.append(8)
    l3.append(7)
    l3.append(2)

    l1.tail.next = l3.head
    l2.tail.next = l3.head

    find_intersection_node(l1, l2)

    l1.display()
    l2.display()
