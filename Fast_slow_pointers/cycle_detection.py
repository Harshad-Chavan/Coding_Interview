from Linked_list.Linked_list_utils import ListNode


def cycle_detection(node1: ListNode) -> ListNode:
    fast_ptr = node1
    slow_ptr = node1
    while fast_ptr and fast_ptr.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr == slow_ptr:
            return True

    return False


if __name__ == "__main__":
    # Create a simple linked list with a cycle
    print("=== Creating a Linked List with a Cycle ===\n")

    # Create nodes manually
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    # Link nodes sequentially: 1 -> 2 -> 3 -> 4 -> 5
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Create cycle: connect node5 back to node2
    # node5.next = node2

    print("Linked List structure:")
    print("1 -> 2 -> 3 -> 4 -> 5 -> (back to 2) [CYCLE]")
    print("\nNode connections:")
    print(f"node1.next = node2 (value: {node1.next.val})")
    print(f"node2.next = node3 (value: {node2.next.val})")
    print(f"node3.next = node4 (value: {node3.next.val})")
    print(f"node4.next = node5 (value: {node4.next.val})")
    # print(f"node5.next = node2 (value: {node5.next.val}) [CYCLE POINT]")

    print(cycle_detection(node1))
