'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        tmp = result
        while l1 and l2:
            num = l1.val+l2.val+carry
            if num>=10:
                carry = 1
                num = num-10
            else:
                carry = 0
            result.next = ListNode(num)
            l1, l2 = l1.next, l2.next
            result = result.next
        while l1:
            result.next = ListNode((l1.val+carry)%10)
            if l1.val+carry>=10:
                carry=1
            else: carry = 0
            result = result.next
            l1 = l1.next
        while l2:
            result.next = ListNode((l2.val+carry)%10)
            if l2.val+carry>=10:
                carry = 1
            else:
                carry = 0
            result = result.next
            l2 = l2.next
        if carry and not l1 and not l2:
            result.next = ListNode(1)
            
        tmp = tmp.next      
        return tmp
