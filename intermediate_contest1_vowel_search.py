def solve(A,B):
    n=len(A)
    pf_array=[]
    sum_val=0
    for i in range(n):
        if A[i] in {'a','e','i','o','u'}:
            sum_val+=1
        pf_array.append(sum_val)
        
    #print(pf_array)
    output_list=[]
    for b in B:
        start,end=b
        
        if start == 0 :
            output_list.append(pf_array[end])
            #print(pf_array[end])
        else:
            output_list.append(pf_array[end]-pf_array[start-1])
            #print(pf_array[end]-pf_array[start])
            
    return output_list

# print(solve("scaler",[[0,2],[2,4]]))
print(solve("interviewbit",[[0,4],[9,10]]))