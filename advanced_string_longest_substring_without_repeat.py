class Solution:
	# @param A : string
	# @return an integer
    def lengthOfLongestSubstring(self, A):
        i=0
        j=0
        n=len(A)
        ans=0
        hash_set=set()
        while j<n:
            if A[j] in hash_set:
                hash_set.remove(A[i])
                i+=1
            else:
                hash_set.add(A[j])
                j+=1
                ans=max(ans,len(hash_set))
        

        return ans