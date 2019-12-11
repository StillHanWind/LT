"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""

from utils.utils_list import generate_list, traversal_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return ListNode(0)

        t = head
        length = 1
        while t.next:
            t = t.next
            length += 1
        t.next = head
        k = k % length

        for _ in range(length-k):
            head = head.next
        t = head

        for _ in range(length-1):
            t = t.next
        t.next = None

        return head


def main():
    head = generate_list([1, 2, 3, 4, 5], ListNode)
    k = 0
    obj = Solution()
    head = obj.rotateRight(head, k)
    traversal_list(head)


if __name__ == '__main__':
    main()
