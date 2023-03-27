# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
# There are 2 approaches to solving this problem.

# Approach 1: Using hashmap.
# Use a hashmap to store the mapping from oldListNode to the newListNode. 
# Whenever you encounter a new node in the oldListNode (either via a random pointer
# or through the next pointer ), create the newListNode, store the mapping. 
# And update the next and random pointers of the newListNode using the mapping from the hashmap.

# Approach 2 : Using 2 traversals of the list.
# Step 1: create a new node for each existing node and join them together 
# eg: A->B->C will be A->A’->B->B’->C->C’

# Step2: copy the random links: for each new node n’, n’.random = n.random.next

# Step3: detach the list: basically n.next = n.next.next; n’.next = n’.next.next
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    
    ####################OPTIMAL APPROACH#############################
    #TC:O(n),SC:O(1)
    def copyRandomList(self, head):
        if not head:
            return None

        cur=head
        #first we addin the duplicate nodes in the linked list

        while cur is not None:
            tmp=RandomListNode(cur.label)
            tmp.next=cur.next
            cur.next=tmp
            cur=cur.next.next

        #now we populate the random values in the alternate nodes

        node=head
        # In this code, we start by setting the current node to the head of the original linked list. 
        # We then iterate over the linked list, processing every other node. This is because the 
        # original linked list and its copy alternate in the linked list.

        # Inside the loop, we check if the random pointer of the current node in the original 
        # linked list is not None. If it's not None, we set the random pointer of the 
        # corresponding node's copy (which is the next node in the linked list) to the node 
        # pointed to by the random pointer in the original linked list's node (which is also 
        # the next node in the linked list).

        # The reason why we set the random pointer of the copy node to the next node pointed 
        # to by the original node's random pointer is that we have already created a copy of 
        # that node, and its memory location is different from the original node's location. 
        # So, we need to update the copy node's random pointer to point to the corresponding 
        # node in the copied linked list.

        # Overall, the second traversal takes O(n) time, where n is the number of nodes in 
        # the linked list. This is because we traverse every other node in the linked list, 
        # and each iteration takes constant time, except for the check for the random pointer 
        # being not None, which also takes constant time.
        while node:
            if node.random:
                node.next.random=node.random.next
            node=node.next.next
            

        #Now we decouple the deep copied nodes

        
        
        

        head=head.next
        dup=head
        #weaving original list out of duplicate and returning the duplicate from head.next

        while dup.next is not None:
            dup.next=dup.next.next
            dup=dup.next
        
        return head
    
    ###########Alternate Approach with Hash map####################
    
    # def copyRandomList(self, head):
    #     memory = {}

    #     new_head = RandomListNode(head.label)

    #     curr = head.next
    #     new_curr = new_head

    #     memory[head] = new_head

    #     while curr:
    #         node = RandomListNode(curr.label)
    #         memory[curr] = node
    #         new_curr.next = node

    #         curr = curr.next
    #         new_curr = node

    #     curr = head
    #     new_curr = new_head

    #     while curr:
    #         if curr.random:
    #             new_curr.random = memory[curr.random]
    #         curr = curr.next
    #         new_curr = new_curr.next

    #     return new_head



        

    


        
