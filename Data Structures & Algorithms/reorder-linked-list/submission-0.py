# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #setup modifiable node
        slow, fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is now at half way point, reverse second half
        second = slow.next #need to store it at node after slow
        prev = slow.next = None #perform actual split

        while second:
            temp = second.next
            second.next = prev#null in beginning
            prev = second
            second = temp

        #second half has been reversed, need to merge
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2