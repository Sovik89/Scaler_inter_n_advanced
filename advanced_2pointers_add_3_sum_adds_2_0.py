def threeSum( A):
        A.sort()
        
        n=len(A)
        
        list_output=list()
        #ans=0
        hash_set=set()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                sum_val=A[i]+A[j]+A[k]            
                
                
                # temp=abs(sum_val-B)
                
                if sum_val==0:
                    if tuple([A[i],A[j],A[k]]) not in hash_set:
                        hash_set.add(tuple([A[i],A[j],A[k]]))
                        list_output.append([A[i],A[j],A[k]])
                    j+=1
                    
                   
                
                elif sum_val<0:
                    j+=1
                else:
                    k-=1
        
        return list_output
    
    
print(threeSum([-1,0,1,2,-1,4]))