# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
    def reverseBetween(self, A, B, C):
     
        count=1
    
        head=A
        cur=A
        
        while count<B:
            cur=cur.next
        
         
    
    
     
     