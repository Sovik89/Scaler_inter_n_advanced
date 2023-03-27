class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers

    def anagrams(self, A):
        hash_ord=dict()
        output_list=[]
        index=1
        for a in A:
            n=len(a)
            st="".join(sorted(a))
            
            if st not in hash_ord:
                hash_ord[st]=[index]
            else:
                hash_ord[st].append(index)
            index+=1
        
        for orders in hash_ord:
            if len(hash_ord[orders])>=1:
                output_list.append(hash_ord[orders])
    
        return output_list