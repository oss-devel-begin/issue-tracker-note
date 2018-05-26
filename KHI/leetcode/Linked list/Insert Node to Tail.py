def Insert(head, data):
    temp = head
    if head is None :
        temp = Node(data)
        print(data)
        return head
    else :
        if temp.next is None:
            temp.next = Node(data)
            print(data)
            return head
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)
            print(data)
            return head