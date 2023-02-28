# Given a matrix A of size Nx3 representing operations. Your task is to design the
# linked list based on these operations.

# There are four types of operations:

# 0 x -1: Add a node of value x before the first element of the linked list. 
# After the insertion, the new node will be the first node of the linked list.
# 1 x -1: Append a node of value x to the last element of the linked list.
# 2 x index: Add a node of value x before the indexth node in the linked list. 
# If index equals to the length of linked list, the node will be appended to the end of linked list.
# If index is greater than the length, the node will not be inserted.
# 3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation.

# A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

# Note: Indexing is 0 based.

# Input type:

# A = [       [0, 1, -1]
#             [1, 2, -1]
#             [2, 3,  1]   ]

########################Alternate Solution #########################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
# class LL:
#     def __init__(self):
#         self.head = None
#         self.length = 0
       
#     def insertfront(self,val):
#         newNode = ListNode(val)
#         if self.head:
#             newNode.next = self.head
#             self.head = newNode
#             self.length += 1
#         else:
#             self.head = newNode
#             self.length += 1
           
#     def insertend(self,val):
#         newNode = ListNode(val)
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = newNode
#             self.length += 1
#         else:
#             self.head = newNode
#             self.length += 1
       
           
#     def getlen(self):
#         return self.length
       
#     def insertpos(self,pos,val):
#         newNode = ListNode(val)
#         if pos > self.getlen():
#             return
#         if pos == 0:
#             self.insertfront(val)
#             return

#         c = 0
#         temp = self.head
#         while c < pos -1:
#             temp = temp.next
#             c += 1
#         newNode.next = temp.next
#         temp.next = newNode
#         self.length += 1
       
#     def delete(self,pos):
#         if pos > self.getlen():
#             return
#         temp = self.head
#         if pos == 0:
#             newhead = temp.next
#             self.head = newhead
#             self.length -= 1
#         else:
#             c = 0
#             while c < pos-1:
#                 temp = temp.next
#                 c += 1
#             newval = temp.next.next
#             temp.next = newval
#             self.length -= 1
       

# class Solution:
#     # @param A : list of list of integers
#     # @return the head node in the linked list
#     def solve(self, A):
#         ll = LL()
#         row = len(A)
#         for i in range(row):
#             if A[i][0] == 0 and A[i][2] == -1:
#                 ll.insertfront(A[i][1])
           
#             elif A[i][0] == 1 and A[i][2] == -1:
#                 ll.insertend(A[i][1])


#             elif A[i][0] == 2:
#                 ll.insertpos(A[i][2],A[i][1])

#             elif A[i][0] == 3 and A[i][2] == -1:
#                 ll.delete(A[i][1])

#         return ll.head

###########################Solution###############

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

head=None
list_length=0

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve( A):
        global head
        global list_length
        
        for i in A:
            if i[0] == 0 and i[2]==-1:
                n=ListNode(i[1])
                n.next=head
                head=n
                list_length+=1
            if i[0] == 1 and i[2] == -1:
                n=ListNode(i[1])
                c=0
                l=head
                position = list_length
                if position == 0:
                    n.next=head
                    head=n
                else:                   
                    while c<position-1:
                        l=l.next
                        c+=1
                    l.next=n
                list_length+=1
            if i[0] == 2:
                n = ListNode(i[1])  
                position=i[2]              
                if i[2]>=0 and i[2]<=list_length:
                    if i[2] == 0:
                        n=ListNode(i[1])
                        n.next=head
                        head=n
                        
                    else:    
                        count = 0
                        prev = head
                        # traverse till the previous node
                        while count < position-1:
                            prev = prev.next
                            count += 1
                        n.next = prev.next
                        prev.next = n
                list_length+=1
            
            if i[0] ==3 and i[2] == -1:
                if i[1]>=0 and i[1]<=list_length and list_length!=0:
                    #temp = None
                    # remove at head
                    if i[1] == 0:
                        #temp = head
                        head = head.next
                    else:
                        count = 0
                        prev = head
                        # traverse till the previous node
                        while count < i[1] -1:
                            prev = prev.next
                            count += 1
                        #temp = prev.next
                        prev.next = prev.next.next
                
                else:
                    continue
                list_length -= 1
                    
        return head
                    
                    
                
                
#head=Solution.solve([[0, 1, -1],[1, 2, -1],[2, 3,  1]])
#head=Solution.solve([[0, 1, -1],[1, 2, -1],[2, 3, 1],[0, 4, -1],[3, 1, -1],[3, 2, -1]  ])
# head=Solution.solve([[1, 13, -1],[3, 0, -1],[3, 1, -1],[2, 15, 0],[3, 0, -1],[1, 12, -1],[3, 0, -1],
#   [1, 19, -1],
#   [1, 13, -1],
#   [3, 0, -1],
#   [0, 12, -1],
#   [1, 13, -1],
#   [3, 2, -1]])
head=Solution.solve([  [2, 18, 0],
  [2, 5, 1],
  [2, 8, 0],
  [1, 7, -1],
  [1, 5, -1],
])




l=head

while l != None:
    print(l.val,end=" ")
    l=l.next
print()
          
                
            
                    
        
        