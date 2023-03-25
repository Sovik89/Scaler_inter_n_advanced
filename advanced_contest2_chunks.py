def solve(A):
        current_sum=0
        original_sum=0
        n=len(A)
        chunks=0
        for i in range(n):
            current_sum+=A[i]
            original_sum+=i
            if current_sum==original_sum:
                chunks+=1
            
        return chunks