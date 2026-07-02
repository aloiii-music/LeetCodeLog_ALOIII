# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        #step 1 -- find left posiition
        dummy = ListNode(0,head)
        leftprev,cur = dummy, head
        for i in range(left-1):
            leftprev, cur = cur, cur.next
        
        #Step 2 portion reversal
        prev = None 
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev,cur =cur, tmp
        
        #Step 3 Clean Up 
        leftprev.next.next = cur 
        leftprev.next = prev

        return dummy.next
            