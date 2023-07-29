from linked_list import ListNode


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # if not head:
    #     return None

    # newNext = head.next
    # if newNext:
    #     temp = reverseList(head.next)
    #     head.next.next = temp
    #     print(temp)
    # newNext = head

    # return head

    # time comp O(N) space comp O(1)
    prev = None
    node = head

    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    return prev

    # time comp O(N) space comp O(N + N)
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
