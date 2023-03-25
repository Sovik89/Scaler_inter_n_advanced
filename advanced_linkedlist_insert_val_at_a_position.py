# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def solve(A, B, C):
    # @param A : head node of linked list
    # @param B : integer->value
    # @param C : integer->0 based position
    # @return the head node in the linked list
        newnode=ListNode(B)
        head=A
        tail=A
        list_length=0
        
        while tail.next!= None:
            list_length+=1
            tail=tail.next
            
            
        if C<=0:
            newnode.next=head.next
            head=newnode
        elif C>=list_length:
            tail.next=newnode
            
        else:
            position=0
            cur=A
            while position <=C-1:
                if position == C-1:
                    newnode.next=cur.next
                    cur.next=newnode
                
                cur=cur.next
                position+=1
        
        return head
    