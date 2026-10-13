# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #create a set of nodes to track which have been seen
        seen = set()
        cur = head

        #loop through linked list and check if seen, if yet its a cycle: return true, at the end of the list return false

        while cur:
            if cur in seen:
                return True
            seen.add(cur)

            cur = cur.next
        
        return False
        