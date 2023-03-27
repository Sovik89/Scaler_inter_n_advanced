class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def minWindow(self, A, B):
        hash_B=dict()
        hash_A=dict()
        n=len(A)
        m=len(B)
        counter=0
        min_length_count=float('inf')
        #populate hash_b
        for i in range(m):
            if B[i] not in hash_B:
                hash_B[B[i]]=1
            else:
                hash_B[B[i]]+=1
        i=0
        j=0
        final_start=-1
        final_end=-1
        while j<n and i<n :
            if A[j] in hash_B:
                if A[j] in hash_A:
                    hash_A[A[j]]+=1
                else:
                    hash_A[A[j]]=1
            # if we are adding an element that is required in the frequency then we increase counter
            # if we have A=1 hashmap_b but we had 2 A's in hashmap_a. Then for first A we increase the counter 
            # but for second A we do not as it is an extra. 
            # This is why we check if the freq is less or equal to what is required then we increase counter else not 
            
                if hash_A[A[j]]<=hash_B[A[j]]:
                    counter +=1
            j+=1
            
            while i<j and counter==len(B):
                if j-i<min_length_count:
                    min_length_count=j-i
                    final_end=j
                    final_start=i
                if A[i] in hash_B:
                    hash_A[A[i]]-=1
                    # to verify if the element we have removed, if it has reduced the freq requied
                    # in that case we decrease to counter to tell the program that we need to add more elements
                    if hash_A[A[i]]<hash_B[A[i]]:
                        counter-=1
                i+=1
            
        if final_start==-1 and final_end==-1:
            return ""
        else:
            return A[final_start:final_end]