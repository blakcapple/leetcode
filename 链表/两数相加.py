# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        cur = head 
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0 
            sum = n1 + n2 + carry
            carry = 0
            if sum >= 10:
                sum -= 10
                carry = 1
            cur.next = ListNode(val=sum)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            # 有carry则再创建一个节点
            if not l1 and not l2 and carry:
                cur.next = ListNode(val=carry)
        return head.next     
                
            
