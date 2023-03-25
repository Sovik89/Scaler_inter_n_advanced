# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        #edge case
        if A==None or A.next == None:
            return A
        
        #rabbit and tortoise
        fast=A
        slow=A
        is_cycle_present=0
        
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                is_cycle_present=1
                break
        
        if is_cycle_present==0:
            return A
        
        s1=A
        s2=slow
        slow_prev=None
        
        while s1!=s2:
            slow_prev=s2
            s1=s1.next
            s2=s2.next
            
        slow_prev.next=None
        
        return A
        
        
            
        
        
        