from linked_list import ListNode
from typing import Optional


def mergeTwoLists(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> Optional[ListNode]:
    # time comp O(max(N, M)) space comp O(1)
    node1 = list1
    node2 = list2
    dummy = ListNode()
    tail = dummy
    while node1 and node2:
        if node1.val <= node2.val:
            tail.next = ListNode(node1.val)
            node1 = node1.next
        else:
            tail.next = ListNode(node2.val)
            node2 = node2.next
        tail = tail.next

    if node1:
        tail.next = node1
    if node2:
        tail.next = node2

    return dummy.next


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    list1_linkedList = ListNode()
    list1_linkedList.add_nodes(list1)

    list2_linkedList = ListNode()
    list2_linkedList.add_nodes(list2)

    print("Input List1")
    list1_linkedList.print_nodes()
    print("Input List2")
    list2_linkedList.print_nodes()

    res = mergeTwoLists(list1_linkedList.next, list2_linkedList.next)
    print("Output")
    res.print_nodes()
