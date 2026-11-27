# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = ListNode(None, head)
        curr = list1
        curr2 = list2
        
        while curr and curr2:
            if curr.val <= curr2.val:
                head.next = curr
                curr = curr.next
                head = head.next
            else:
                head.next = curr2
                curr2 = curr2.next
                head = head.next
        if curr:
            head.next = curr
        if curr2:
            head.next = curr2
        return tail.next.next
    