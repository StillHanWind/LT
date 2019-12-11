"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
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
        result = None
        for i in range(len(lists)):
            result = mergeTwoLists(result, lists[i])
        return result


def main():
    lists = list()
    t = ListNode(1)
    t.next = ListNode(4)
    t.next.next = ListNode(5)
    lists.append(t)
    t = ListNode(1)
    t.next = ListNode(3)
    t.next.next = ListNode(4)
    lists.append(t)
    t = ListNode(2)
    t.next = ListNode(6)
    lists.append(t)
    s = Solution()
    head = s.mergeKLists(lists)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
