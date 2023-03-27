#Input
"""
2   ->  4 
|       |       
7      11    
|            
7
"""

#O/P:

# 2 -> 4 -> 7 -> 7 -> 11

#Return Flattened sorted list


#########################################CODE########################################


class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None

# @param root: ListNode
# @return ListNode

def mergeList(a,b):
    #here we check recursively which value is smallest among a and b and append it to ans recursievely
    # it will be caught by any of the ans in the a.val or b.val and we will return that ans
    #base case if a==None we return b(meaning a is exhausted we return b) and vice versa
    if a is None:
        return b
    if b is None:
        return b
    if a.val<b.val:
        ans=a
        ans.down=mergeList(a.down,b)    
    else:
        ans=b
        ans.down=mergeList(b.down,a)

    return ans  
    
def flatten(root):
    #We check recursievely to the last two lists in the right direction and we merge them
    #if root ==None or root.right ==None we return root
    if root==None or root.right==None:
        return root
    
    root.right=flatten(root.right)
    
    root=mergeList(root,root.right)
    
    return root



"""
L1->L2->L3->L4->L5

steps:
L4=merge(L4,L5)
L3=merge(L3,L4)
L2=merge(L2,L3)
L1=merge(L1,L2)

return L1

T.C:O(Summation:of all nodes in the nested Linked List)
S.C:O(1)

"""