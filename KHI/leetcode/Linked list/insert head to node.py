def Insert(head, data):
    if head is None:
        head = Node(data)
        return head
    else :
        temp = Node(data)
        temp, head = head, temp
        head.next = temp
        return head