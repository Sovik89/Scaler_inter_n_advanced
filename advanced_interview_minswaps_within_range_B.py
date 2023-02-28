def solve(A, B):
    correct_range=0
    n = len(A)
    #val_present=0
    swap_count=0
    ans=0
    for i in range(n):
        if A[i]<=B:
            correct_range+=1
    # print(correct_range)
    for i in range(correct_range):
        if A[i]>B:
            swap_count+=1
    ans=swap_count
    for i in range(correct_range,n):
        if A[i-correct_range]>B:
            swap_count-=1
        if A[i]>B:
            swap_count+=1
        ans=min(ans,swap_count)
        
        
    # print(val_present)
    # for i in range(correct_range,n):
    #     if A[i]<=B:
    #         val_outside+=1
    # print(val_outside)       
    return ans


print(solve([1, 12, 10, 3, 14, 10, 5],8))
#print(solve([5, 17, 100, 11],20))

# print(solve([ 52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 
#              24, 74, 92, 5, 84, 27, 48, 49, 37, 59, 3, 56, 79, 26, 55, 60, 16,
#              83, 63, 40, 55, 9, 96, 29, 7, 22, 27, 74, 78, 38, 11, 65, 29, 52, 
#              36, 21, 94, 46, 52, 47, 87, 33, 87, 70 ],19))
        
    
    