class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add_nodes(self, nodes):
        root = self
        for node in nodes:
            root.next = ListNode(node)
            root = root.next

    def print_nodes(self):
        root = self
        print("Linked List", end=": ")
        while root:
            print(root.val, end=" ")
            root = root.next
        print()
