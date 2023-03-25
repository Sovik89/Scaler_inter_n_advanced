# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        head=A
        if head==None:
            return 0
        
        count=0
        
        cur=head
        
        while cur is not None:
            if count==B:
                return cur.val
            cur=cur.next
            count+=1
            
        