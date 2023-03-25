def solve(A, B):
    n=len(A)
    p1=0
    p2=n-1
    mod=10**9+7
    ans=0
    while p1<p2:
        if A[p1]+A[p2]>B:
            p2-=1
        elif A[p1]+A[p2]<B:
            p1+=1
        else:
            if A[p1]==A[p2]:
                #there is no element which is greater than or less than the value and every value is valid
                x=p2-p1+1
                ans+=((x*(x-1))//2)%mod
                break
            else:
                dup1 = 1
                p1 += 1
                while A[p1] == A[p1 - 1]:
                    p1 += 1
                    dup1 += 1

                dup2 = 1
                p2 -= 1
                while A[p2] == A[p2 + 1]:
                    p2 -= 1
                    dup2 += 1

                ans += (dup1 * dup2) % mod
        
    
    return ans%mod


#print(solve([1,1,1],2))
print(solve([3,7,8,12,19],15))
            
        
        