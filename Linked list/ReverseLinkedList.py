from linked_list import ListNode


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    temp = []
    node = head
    while node:
        temp.append(node.val)
        node = node.next

    dummy = ListNode()
    tail = dummy

    for n in temp[::-1]:
        tail.next = ListNode(n)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    head = ListNode()
    head.add_nodes([1, 2, 3, 4, 5])
    print("Input")
    head.next.print_nodes()
    res = reverseList(head.next)
    print("Output")
    res.print_nodes()
