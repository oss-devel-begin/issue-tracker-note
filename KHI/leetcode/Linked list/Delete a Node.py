def Delete(head, position):
    if head is None or head.next is None:
        head = None
        return head
    else:
        current = head
        #원하는 위치 전으로 가기
        for i in range(position-1):
            current = current.next
        #해당하는 위치를 지우고, 좌측과 우측 리스트 이어주기
        if current is head:#맨앞
            head = head.next
        elif current.next.next is not None:#가운데
            current.next = current.next.next
        #만일 이을 수 없다면, 그냥 None값 주기
        else :#맨뒤
            current.next = None
        return head