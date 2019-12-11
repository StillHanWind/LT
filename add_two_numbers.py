"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        t = result
        j = 0
        while l1 or l2 or j:
            if l1:
                t.val += l1.val
                l1 = l1.next
            if l2:
                t.val += l2.val
                l2 = l2.next
            t.val += j
            j = t.val // 10
            t.val %= 10
            if j or l1 or l2:
                t.next = ListNode(0)
                t = t.next
        return result


def main():
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    l1 = ListNode(5)
    l2 = ListNode(5)
    s = Solution1()
    result = s.addTwoNumbers(l1, l2)
    print(result.val)
    print(result.next.val)
    # print(result.next.next.val)


if __name__ == '__main__':
    main()
