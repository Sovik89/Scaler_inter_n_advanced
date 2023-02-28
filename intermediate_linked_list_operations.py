# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and 
# a pointer to the next node. It should support the following operations:

# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space.
# Note:

# If an input position does not satisfy the constraint, no action is required.
# Each print query has to be executed in a new line.

################################   Primary Solutuion    #########################

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = None
size_of_ll = 0


def insert_node(position, value):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll + 1:
        temp = ListNode(value)
        # insert at head
        if position == 1:
            temp.next = head
            head = temp
        else:
            count = 1
            prev = head
            # traverse till the previous node
            while count < position - 1:
                prev = prev.next
                count += 1
            temp.next = prev.next
            prev.next = temp
        size_of_ll += 1


def delete_node(position):
    global head
    global size_of_ll
    if position >= 1 and position <= size_of_ll:
        temp = None
        # remove at head
        if position == 1:
            temp = head
            head = head.next
        else:
            count = 1
            prev = head
            # traverse till the previous node
            while count < position - 1:
                prev = prev.next
                count += 1
            temp = prev.next
            prev.next = prev.next.next
        size_of_ll -= 1


def print_ll():
    global head
    tmp = head
    ans = []
    # traverse the entire linked list
    while tmp is not None:
        ans.append(str(tmp.val))
        tmp = tmp.next
    print(" ".join(ans))
    
    
################  Alternate Solution 1   ######################

# class Node:
#     def __init__(self,data,next= None):
#         self.data = data
#         self.next = next


# class LL:
#     def __init__(self):
#         self.head = None
#         self.length = 0


#     def insert_node(self,position, value):
#         if position > (self.length + 1):
#             return
           
#         newNode = Node(value)
#         temp = self.head
#         if position == 1:
#             newNode.next = temp
#             self.head = newNode
#         else:            
#             c = 1
#             while c < position -1:
#                 temp = temp.next
#                 c += 1
#             newNode.next = temp.next
#             temp.next = newNode
#         self.length += 1      
       

#     def delete_node(self,position):
#         if position > (self.length):
#             return
#         else:
#             temp = self.head
#             if position == 1:
#                 newHead = temp.next
#                 self.head = newHead

#             else:
#                 count = 1
#                 while count < position - 1:
#                     temp = temp.next
#                     count +=1

#                 new_node = temp.next.next
#                 temp.next = new_node
               
           
#             self.length -= 1

#     def print_ll(self):
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 print(temp.data,end= " ")
#                 temp = temp.next

#             if temp:
#                 print(temp.data,end= "")
#             print()




# ll  = LL()


# def insert_node(position, value):
#     return ll.insert_node(position,value)


# def delete_node(position):
#     return ll.delete_node(position)

# def print_ll():
#     return ll.print_ll()



###################    Alternate Solution   ##############################

##########Preferred approach  ############

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size_of_ll = 0
        
#     def insert_at(self,position, value):
        
#         if position > (self.size_of_ll+1):
#             return
        
#         if position >= 1 and position <= self.size_of_ll + 1:
#             temp = ListNode(value)
#             # insert at head
#             if position == 1:
#                 temp.next = self.head
#                 self.head = temp
#             else:
#                 count = 1
#                 prev = self.head
#                 # traverse till the previous node
#                 while count < position - 1:
#                     prev = prev.next
#                     count += 1
#                 temp.next = prev.next
#                 prev.next = temp
#             self.size_of_ll += 1
    
#     def delete_at(self,position):
        
#         if position > (self.size_of_ll+1):
#             return
        
#         if position >= 1 and position <= self.size_of_ll:
#             temp = None
#             # remove at head
#             if position == 1:
#                 temp = self.head
#                 self.head = self.head.next
#             else:
#                 count = 1
#                 prev = self.head
#                 # traverse till the previous node
#                 while count < position - 1:
#                     prev = prev.next
#                     count += 1
#                 temp = prev.next
#                 prev.next = prev.next.next
#             self.size_of_ll -= 1
    
#     def print_linked_list(self):
#         #global head
#         tmp = self.head
#         ans = []
#         # traverse the entire linked list
#         while tmp is not None:
#             ans.append(str(tmp.val))
#             tmp = tmp.next
#         print(" ".join(ans))
        
        

# ll = LinkedList()

# def insert_node(position, value):
#     ll.insert_at(position,value)


# def delete_node(position):
#     ll.delete_at(position)


# def print_ll():
#     ll.print_linked_list()
    
    

insert_node(1,23)
insert_node(2,24)
print_ll()
delete_node(1)
print_ll()