# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        head=A
        
        if head.next == None:
            return 1
        
        cur=head
        
        while cur.next is not None:
            if cur.val > cur.next.val:
                return 0
            cur=cur.next
        
        return 1
            
            
        