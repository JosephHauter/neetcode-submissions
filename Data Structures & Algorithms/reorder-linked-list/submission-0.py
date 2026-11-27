# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 1. Find middle and split
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = slow.next
        slow.next = None

        # 2. Reverse second half
        prev = None

        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp

        # 3. Merge by alternating
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
