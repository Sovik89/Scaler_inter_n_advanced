'''
Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None
'''
class Solution:
    def getIntersectionNode(self, A, B):
        if A==None or B==None:
            return None
        
         
        
        headA=A
        headB=B
        length_A=1
        length_B=1
        tailA=A
        tailB=B
        
        #length of A
        
        while tailA!=None:
            tailA=tailA.next
            length_A+=1
        
        
        #length of B
        while tailB!=None:
            tailB=tailB.next
            length_B+=1
        
        effectieve_lenght=abs(length_B-length_A)
        
        if length_A>length_B:
            i=0
            while i<effectieve_lenght:
                headA=headA.next
                i+=1
        if length_A<length_B:
            i=0
            while i<effectieve_lenght:
                headB=headB.next
                i+=1
        
        while headA!=None:

            if headA==headB:
                return headA
            
            headA=headA.next
            headB=headB.next
            
            
            
        return None