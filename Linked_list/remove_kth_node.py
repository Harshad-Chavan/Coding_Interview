from Linked_list_utils import *


def remove_kth_node(l1, k):
    l1.display()

    # create a dummy node
    l1.prepend("dummy")

    # place the leader and trailer pointer
    trailer = l1.head
    leader = l1.head

    # move leader k steps ahead
    for _ in range(k):
        leader = leader.next

        # if k is larger than the length of list.leadr will be none
        if not leader:
            print("k is larger than length of list")
            return

    # move both together till leader reached end
    while leader.next:
        trailer = trailer.next
        leader = leader.next

    # Do the deletion
    trailer.next = trailer.next.next
    l1.head = l1.head.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.create(1)
    for i in range(2, 7):
        l1.append(i)
    remove_kth_node(l1, 8)
    l1.display()
