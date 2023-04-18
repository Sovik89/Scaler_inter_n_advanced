def t2Sum( B):

        list_val=[7,10,9,20]
        #self.inorder(A,list_val)

        n=len(list_val)

        hash_map=dict()

        for i in range(n):
            hash_map[list_val[i]]=i
            
        for j in range(n):
            val=B-list_val[j]
            if val in hash_map:
                if val*2!=B:
                    return 1


        return 0
    
    
    
print(t2Sum(40))
            
            
        

    
    
