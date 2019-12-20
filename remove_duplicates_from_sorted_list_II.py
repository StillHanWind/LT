"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
"""

from utils.utils_list import generate_list, traversal_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode(None)
        pre.next = head
        t_pre = pre
        tag = False
        while t_pre.next:
            if t_pre.next.next and t_pre.next.val == t_pre.next.next.val:
                tag = True
                t_pre.next.next = t_pre.next.next.next
            else:
                if tag:
                    t_pre.next = t_pre.next.next
                    tag = False
                else:
                    t_pre = t_pre.next
        return pre.next


def main():
    head = generate_list([1, 2, 3, 3, 4, 4, 5], ListNode)
    traversal_list(head)
    obj = Solution()
    head = obj.deleteDuplicates(head)
    traversal_list(head)


if __name__ == '__main__':
    main()
