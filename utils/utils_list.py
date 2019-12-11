def generate_list(li, node):
    if not li:
        return None
    head = node(li[0])
    t = head
    for i in li[1:]:
        t.next = node(i)
        t = t.next
    return head


def traversal_list(head):
    while head:
        print(head.val)
        head = head.next
