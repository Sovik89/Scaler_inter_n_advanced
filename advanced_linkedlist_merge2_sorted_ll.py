# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        head1=A
        head2=B
        head=None
        tail=None
        
        #edge cases
        if head1 == None and head2!= None:
            return head2
        if head1!=None and head2== None:
            return head1
        if head1==None and head2 == None:
            return []
        
        if head1.val<=head2.val:
            head=head1
            tail=head1
            head1=head1.next
        else:
            
            head=head2
            tail=head2
            head2=head2.next
        
        #main body    
        while head1 and head2:
            if head1.val<=head2.val:
                tail.next=head1
                tail=tail.next
                head1=head1.next
            else:
                tail.next=head2
                tail=tail.next
                head2=head2.next
                
        #residuals
        
        if head1!= None:
            tail.next=head1
        if head2!=None:
            tail.next=head2
        
        return head