# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        head=A
        tail=head
        length=1#We have constrataints starting from 1 value
        while tail.next is not None:
            tail=tail.next
            length+=1
        
        cur=head
        
        if B>= length:
            head=head.next
            return head
        if length == 1:
            return None
        
        effective_length_to_search=length-B
        
        i=1
        
        
        while i<effective_length_to_search:
            if cur.next.next ==None:
                cur.next=None
                return head
            
            cur=cur.next
            i+=1
        
        cur.next=cur.next.next
        
        return head
