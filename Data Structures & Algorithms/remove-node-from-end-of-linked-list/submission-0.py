# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #need to make two pointers offset by n (+1 since we want L right before it, this is what dummy for)
        dummy = ListNode(0, head)
        left,right = dummy, head

        #need to loop through n to make right = n offset
        while right and n > 0:
            right = right.next
            n -= 1

        #right is at offset, need to loop till right is at end
        while right:
            left = left.next
            right = right.next

        #left is node right before removal node index n
        #skip left

        left.next = left.next.next

        return dummy.next