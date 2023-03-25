# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        head=A
        prev=None
        cur=A
        while cur != None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
            #head=prev
        head=prev     
        
        
        tmp=head
        while tmp is not None:
            print(tmp.val,end=" ")
            tmp=tmp.next
        print()
        
