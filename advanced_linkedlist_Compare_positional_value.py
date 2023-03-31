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

        head_A=A
        head_B=B
        
        while (head_A is not None) and (head_B is not None):
            if head_A.val!=head_B.val:
                return 0
            head_A=head_A.next
            head_B=head_B.next
        
        return 1