class TrieNode:
    def __init__(self) -> None:
        self.is_end=False
        self.hash_map={}


class Solution:
	# @param A : list of strings
	# @return a list of strings

    
    def insert(self,root,string):
        
        curr=root
        
        for ch in string:
            if ch in curr.hash_map:
                curr=curr.hash_map[ch]
                #curr.is_duplicate=True
            else:
                new_node=TrieNode()
                curr.hash_map[ch]=new_node
                curr=new_node
                #curr.is_duplicate=False
        curr.is_end=True
                
    def search(self,root,string):
        curr=root
        
        #prefix_val=""
        
        for ch in string:
            #prefix_val+=ch
            
            if ch in curr.hash_map:
                curr=curr.hash_map[ch]
            else:
                return 0
        
        if curr.is_end:
            return 1
        else:
            return 0               
        
    
    def solve(self, A, B):
        
        resultant_array=[]
        root=TrieNode()
        
        n=len(A)
        
        for i in range(n):            
            self.insert(root,A[i])
        
        m=len(B)    
        
        for j in range(m):            
            temp_val=self.search(root,B[j])            
            resultant_array.append(temp_val)
            
            
        return resultant_array
            
        
     
     
     


    