from linked_list import ListNode
from typing import Optional, List


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # time comp O(N * M + (N + M)log((N + M))) space comp O(N + M)
    # where N = length of lists, M = max length of lists[i]
    all_nodes = []

    for linked_list in lists:
        cur = linked_list
        while cur:
            all_nodes.append(cur.val)
            cur = cur.next

    all_nodes.sort()

    dummy = ListNode()
    tail = dummy

    for node_val in all_nodes:
        tail.next = ListNode(node_val)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    temp = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for nodes in temp:
        root = ListNode()
        root.add_nodes(nodes)
        lists.append(root.next)

    print("Input", temp)
    res = mergeKLists(lists)
    print("Output")
    res.print_nodes()
