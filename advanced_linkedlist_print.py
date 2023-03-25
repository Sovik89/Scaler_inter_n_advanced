# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        
        node=A

        while node != None:
            print(node.val,end=" ")
            node=node.next

        print()