"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        if not l1 and not l2:
            return None
        if l1.val <= l2.val:
            l = l1
            l1 = l1.next
        else:
            l = l2
            l2 = l2.next
        temp = l
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        return l


def main():
    l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(4)
    l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    s = Solution()
    l = s.mergeTwoLists(l1, l2)
    print(l.val)
    print(l.next.val)
    print(l.next.next.val)
    print(l.next.next.next.val)
    print(l.next.next.next.next.val)
    print(l.next.next.next.next.next.val)


if __name__ == '__main__':
    main()
