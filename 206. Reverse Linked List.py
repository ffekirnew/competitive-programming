# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create pointers
        prev_node = None
        curr_node = head
        # loop through the list
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        # create the object to be returned
        answer = prev_node
        # return the solution object
        return answer
