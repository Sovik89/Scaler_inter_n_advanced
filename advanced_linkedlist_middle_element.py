# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        # head=A
        # if head==None:
        #     return None
        # cur=head
        # rabbit=cur
        # tortoise=cur
        # #if rabbit (mod 2)==0, we return N/2+1
        
        # tmp=head
        # count=0
        # while tmp is not None:
        #     tmp=tmp.next
        #     count+=1
            
        
        # while (rabbit.next is not None) and (rabbit.next.next is not None):
        #     tortoise=tortoise.next
        #     rabbit=rabbit.next.next
        
        # if count%2==0:
        #     return tortoise.next.val
        # else:
        #     return tortoise.val
        
        ################################ALTERNATE APPROACH#####################
        
        head=A

        if head == None:
            return 0

        slow=head
        fast=head        

        while (fast.next is not None) and (fast.next.next is not None):            
            slow=slow.next
            fast=fast.next.next
        
        if fast.next==None:
            return slow.val

        return slow.next.val
            
        