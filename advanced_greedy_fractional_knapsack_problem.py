import heapq

def solve(A, B, C):
        #A is the array of values
        #B is the array of weights
        #C is the knapsack capacity
        max_heap=[]
        n=len(A)
        
        for i in range(n):
                val=A[i]/B[i]
                heapq.heappush(max_heap,(-val,A[i],B[i]))
                
        
        #print
        sum_of_weight=0
        total_val=0
        
        while max_heap:
                o_p=heapq.heappop(max_heap)
                #print(o_p)
                
                effective_val_rem=C-sum_of_weight
                sum_of_weight+=o_p[2]
                if effective_val_rem>=o_p[2]:
                        total_val+=o_p[1]
                else:
                        residual_val=(-o_p[0]*effective_val_rem)
                        total_val+=residual_val
                        break
        ans=int(total_val*1000)
        print(ans)
        residual_variance=ans%10
        ans=ans//10
        if residual_variance>9:
                return ans+1
        else:
                return ans
                
        #return round(total_val*100)

                                
        
                        
print(solve(
        [2,7],
        [11,3],
        7
))

# print(solve(
#         [10, 20, 30, 40],
#         [12, 13, 15, 19],
#         10
# ))

# print(solve([3],[20],17))
