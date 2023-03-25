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
        head=A
        
        if head ==None or head.next ==None:
            return head
        
        #initialize the variables

        prev=None
        cur=head
        i =1

        #keeping the left side of the linkedlist safe from reversal
        while i <B:
            prev=cur
            cur=cur.next
            i+=1

        #Keep the previous and current value safe

        N0=prev
        N1=cur

        prev=None#we use prev afresh

        while i<=C:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
            i+=1


        N1.next=cur
        if N0:
            N0.next=prev
            return A
        else:
            return prev#prev is the head since nothing in the previous exist