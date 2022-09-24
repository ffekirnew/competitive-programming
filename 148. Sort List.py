# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convert(self, list):
        answer = []
        while list:
            answer.append(list.val)
            list = list.next
        return answer
    def convertBack(self, list):
        answer = ListNode()
        curr_node = answer
        for i in range(len(list)):
            curr_node.next = ListNode(list[i])
            curr_node = curr_node.next
        return answer.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        convert = self.convert(head)
        convert.sort()
        return self.convertBack(convert)
