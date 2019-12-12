"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""

from utils.utils_list import generate_list, traversal_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        t = head
        tn = head.next if head and head.next else None
        while tn:
            if t.val == tn.val:
                t.next = tn.next
                tn = t.next
            else:
                t = t.next
                tn = tn.next
        return head


def main():
    head = generate_list([1, 1, 2, 3, 3], ListNode)
    obj = Solution()
    head = obj.deleteDuplicates(head)
    traversal_list(head)


if __name__ == '__main__':
    main()
