from linked_list import ListNode
from typing import Optional


def hasCycle(head: Optional[ListNode]) -> bool:
    # time comp O(N) space comp O(1)
    if not head:
        return False
    slow, fast = head, head.next

    while slow and fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


if __name__ == "__main__":
    head = ListNode()
    head.add_nodes([1, 2, 3, 4, 5])
    # head.next.next.next = head
    print("Input", "1, 2, 3, 4, 5", "cycle is at 3 index")
    res = hasCycle(head.next)
    print("Output", res)
