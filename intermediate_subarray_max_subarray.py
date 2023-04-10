def maxSubarray(self, A, B, C):
        ######################### traditional solution ################# Runtime 715 ms
    
        # max_permissible_sum=0
        # for i in range(0,A):
        #     sum=0
        #     for j in range(i,A):
        #         sum=sum+C[j]
        #         if sum < B:
        #             if sum > max_permissible_sum:
        #                 max_permissible_sum=sum
        #         elif sum == B:
        #             max_permissible_sum=sum
        #             return max_permissible_sum
        
        # if max_permissible_sum == 0:
        #     return 0
        # else:
        #     return max_permissible_sum
        
        ##################### Optimal Solution with 2 pointer ############ Runtime 210 ms
        
        if A==1:
            return C[0]
    
        p1=0
        p2=1
        
        sum_val=C[p1]
        max_sum=0
        while p2!=A :
            
            
            if sum_val == B:
                return sum_val
            elif sum_val>B:
                sum_val-=C[p1]
                p1+=1
                if sum_val<B:
                    max_sum=max(max_sum,sum_val)
            
            else:
                sum_val+=C[p2]
                p2+=1
                if sum_val<B:
                    max_sum=max(max_sum,sum_val)
        
        if sum_val>B:
            while sum_val>B:
                sum_val-=C[p1]
                p1+=1

        max_sum=max(max_sum,sum_val)
                
            
            
        return max_sum