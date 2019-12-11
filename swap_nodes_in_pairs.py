"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head and not head.next:
            return head
        l = head
        r = head.next
        head = r
        l.next = head.next
        head.next = l

        t = ListNode(None)
        l = head
        t.next = l
        r = l.next

        while r.next and r.next.next:
            t = t.next.next
            l = l.next.next
            r = r.next.next
            t.next = r
            l.next = r.next
            r.next = l
            l = t.next
            r = t.next.next
        return head


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    head = s.swapPairs(head)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
