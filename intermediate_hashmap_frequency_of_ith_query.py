# Given an array A. You have some queries given by the array B.
# For the i-th query, find the frequency of B[i] in the array A.

#IP Format:First argument A is an array of integers.
# Second argument B is an array of integers denoting the queries.

#OP Format: Return an array of integers answering each of the queries.

def solve(A,B):
    freq_dict={}
    output_list=list()
    
    for i in range(len(A)):
       if A[i] not in freq_dict:
           freq_dict[A[i]]=1
       else:
           freq_dict[A[i]]+=1  
           
    
    for i in range(len(B)):
        if B[i] in freq_dict:
            output_list.append(freq_dict[B[i]])
        else:
            output_list.append(0)
            
    return output_list


#print(solve([1, 2, 1, 1],[1, 2]))
print(solve([2, 5, 9, 2, 8],[3, 2]))
    