# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reorderList(self, A):
        
        #edgecase
        if A == None or A.next==None:
            return A
        
        
        #Initializations for A1,A2,A3...
        head1=A
        tail1=A
        #first we find the middle of the list using 
        slow=A
        fast=A
        
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        #get the reverse from slow.next
        
        
                
        prev=None
        cur=slow.next
        
        while cur !=None:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        slow.next=prev
        
        head2=prev
        tail2=prev
        
        #we initialize a different Linked list
        
        head3=tail1
        tail1=tail1.next
        tail3=head3
        toggle=True
            
        while tail2!=None:
            if toggle==True:
                tail3.next=tail2
                tail2=tail2.next
                tail3=tail3.next
            else:
                tail3.next=tail1
                tail1=tail1.next
                tail3=tail3.next
            toggle=not(toggle)
                
        if tail1==slow:
            tail3.next=slow
            tail3=tail3.next
        tail3.next=None
            
        return head3
                    
        
        
        
        
        
        
        
        
        
        
     
     