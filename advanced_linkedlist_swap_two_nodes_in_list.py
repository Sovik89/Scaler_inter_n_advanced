# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def swapPairs(self, A):
        head=A
        #edge case
        if head ==None or head.next==None:
            return head
        
        #Initialize
        prev=None#node before current
        cur=head#current as in head
        tmp=cur.next#next value of current
        
        #we check while curis not none or tmp is not none
        while cur is not None and tmp is not None:
            #prev=cur
            cur.next=tmp.next#connect cur with node next to tmp
            tmp.next=cur#connect tmp's next value with curr
            if prev is None:
                head=tmp#we establish head as cur.next when prev == None
            else:
                prev.next=tmp # else if tmp is not head we give the interchanged value next as tmp
            
            
            prev=cur#we keep prev as the current value before we move current cursor
            
            
            
            cur=cur.next#we move current cursor
            
            if cur==None:#if current now is None there is no point in moving further
                break
            tmp=cur.next#if cur.next exit it should be tmp
            
        return head
     
     