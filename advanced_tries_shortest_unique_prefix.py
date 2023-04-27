class TrieNode:
    def __init__(self) -> None:
        self.is_duplicate=True
        self.hash_map={}


class Solution:
	# @param A : list of strings
	# @return a list of strings

    
    def insert(self,root,string):
        
        curr=root
        
        for ch in string:
            if ch in curr.hash_map:
                curr=curr.hash_map[ch]
                curr.is_duplicate=True
            else:
                new_node=TrieNode()
                curr.hash_map[ch]=new_node
                curr=new_node
                curr.is_duplicate=False
                
    def search(self,root,string):
        curr=root
        
        prefix_val=""
        
        for ch in string:
            prefix_val+=ch
            
            if ch in curr.hash_map:
                curr=curr.hash_map[ch]
                if not curr.is_duplicate:
                    break
        
        return prefix_val
            
        
        
                
        
    
    def prefix(self, A):
        
        resultant_array=[]
        root=TrieNode()
        
        n=len(A)
        
        for i in range(n):
            
            self.insert(root,A[i])
            
        
        for j in range(n):
            
            temp_val=self.search(root,A[j])
            
            resultant_array.append(temp_val)
            
            
        return resultant_array
            
        
     
     
     


    