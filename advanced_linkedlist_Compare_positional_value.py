# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return an integer
    def solve(self, A, B):

        maxval,count_A,count_B=0,0,0

        tail_A=A
        tail_B=B

        while tail_A is not None:
            tail_A=tail_A.next
            count_A+=1
        
        while tail_B is not None:
            tail_B=tail_B.next
            count_B+=1

        minval=min(count_A,count_B)

        i=0
        head_A=A
        head_B=B
        while i<minval:
            if head_A.val!=head_B.val:
                return 0
            head_A=head_A.next
            head_B=head_B.next
            i+=1

        return 1