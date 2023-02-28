def solve(A):
    
    
        org_sum=0
        curr_sum=0
        chunk_count=0
        
        n=len(A)
        
        for i in range(n):
            org_sum+=A[i]
            curr_sum+=i

            if org_sum == curr_sum:
                chunk_count+=1
            
        
        
        return chunk_count


#print(solve([1,2,3,4,0]))
print(solve([2,0,1,3,4,6,5]))



        
