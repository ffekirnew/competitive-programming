# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        while head.next != None:
            list.append(head.val)
            head = head.next
        list.append(head.val)
        temp = list[:]
        list.reverse()
        print(temp, list)
        return temp == list