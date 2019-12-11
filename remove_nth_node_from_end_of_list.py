"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        nodes = list()
        while temp:
            nodes.append(temp)
            temp = temp.next
        if nodes[-n] == head:
            head = head.next
        else:
            nodes[-n-1].next = nodes[-n].next
        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp1 = head
        temp2 = head
        for _ in range(n):
            temp2 = temp2.next
        if not temp2:
            head = head.next
            return head
        while temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = temp1.next.next
        return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    n = 2
    s = Solution2()
    head = s.removeNthFromEnd(head, n)
    print(head.val)
    print(head.next.val)
    print(head.next.next.val)
    print(head.next.next.next.val)


if __name__ == '__main__':
    main()
