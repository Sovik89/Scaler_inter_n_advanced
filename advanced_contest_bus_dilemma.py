def solve(A, B):
        sum =0
        ans=0
        n =len(A)
        prefix_array=[]
        #prefix sum
        
        for i in range(n):
            sum+=A[i]
            if sum<=B:
                prefix_array.append(sum)
            else:
                prefix_array.append(0)
            
        pf_max=max(prefix_array)
        pf_min=min(prefix_array)
        
        neg=-pf_min
        
        if neg> B and pf_min!=0:
            return 0
        
        if B == pf_max:
            return 0
        ans=B-pf_max+1
        
        #corner cases
        if pf_min <0:
            ans+=pf_min
        if pf_max<0:
            ans+=pf_max
        
        return ans         
    

print(solve([2,1,-3],5))    