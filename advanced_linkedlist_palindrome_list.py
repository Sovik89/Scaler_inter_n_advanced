# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
    def lPalin(self, A):
        #we use tortoise and rabbit solution
        
        if A==None or A.next==None:
            return 1
        
        head=A
        slow=A
        fast=A
        
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        #We now reverse from mid next/slow next to end
        prev=None
        cur=slow.next
        
        while cur !=None:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        slow.next=prev
        
        head2=prev
        
        while head2!=None:
            if head.val!=head2.val:
                return 0
            head=head.next
            head2=head2.next
        
        return 1
