# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(A, B):
        head=A
        tail=A
        length=0
        while tail.next !=None:
            tail=tail.next
            length+=1
        
        if B<=0:
           head = head.next 
        elif 1<=B<=length:
            position =0
            cur=head
            while position<B-1:
                cur=cur.next
                position+=1
            x=cur.next
            cur.next=x.next
            
        return head