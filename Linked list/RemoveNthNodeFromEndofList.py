from linked_list import ListNode


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # time comp O(N + N + N) space comp O(N + N) res_linkedlist's len + head's len
    temp = []
    cur_node = head

    while cur_node:
        temp.append(cur_node.val)
        cur_node = cur_node.next

    # reversing the temp list
    temp = temp[::-1]
    # marking the nth index to None
    temp[n - 1] = None
    # reversing the temp list to original form
    temp = temp[::-1]

    new_head = ListNode()
    tail = new_head

    for n in temp:
        # must check is not None because zero is also considered as a False
        if n is not None:
            tail.next = ListNode(n)
            tail = tail.next

    return new_head.next


if __name__ == "__main__":
    head = ListNode()
    head.add_nodes([1, 2, 3, 4, 5])
    n = 2
    print("Input", f"n: {n}")
    head.next.print_nodes()
    res = removeNthFromEnd(head.next, n=n)
    print("Output")
    res.print_nodes()
