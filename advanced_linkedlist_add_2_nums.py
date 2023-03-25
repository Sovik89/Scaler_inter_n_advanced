#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        #headA=A
        tailA=A
        #headB=B
        tailB=B
        
        lengthA,lengthB=1,1
        
        while tailA != None:
            tailA=tailA.next
            lengthA+=1
            
        while tailB != None:
            tailB=tailB.next
            lengthB+=1
        
        bigger_num_list,smaller_num_list=(A,B) if lengthA>=lengthB else (B,A)
        
        head3=None
        tail3=None
        carry_forward=0
        while smaller_num_list !=None:
            value=bigger_num_list.val+smaller_num_list.val+carry_forward
            
            effectieve_value=value%10
            carry_forward=value//10
            
            new_node=ListNode(effectieve_value)
            
            if head3==None:
                head3=new_node
                tail3=head3
            else:
                tail3.next=new_node
                tail3=tail3.next
                
            bigger_num_list=bigger_num_list.next
            smaller_num_list=smaller_num_list.next
            
        
        while bigger_num_list!=None:
            value=bigger_num_list.val+carry_forward
            
            effectieve_value=value%10
            
            carry_forward=value//10
            
            new_node=ListNode(effectieve_value)
            tail3.next=new_node
            tail3=tail3.next
            
            bigger_num_list=bigger_num_list.next
            
        if carry_forward!=0:
            tail3.next=ListNode(carry_forward)
            tail3=tail3.next
            
        tail3.next=None
        
        return head3
            
        
            
                    
         