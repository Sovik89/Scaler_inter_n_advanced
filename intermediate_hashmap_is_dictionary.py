# Surprisingly, in an alien language, they also use English lowercase letters, 
# but possibly in a different order. The order of the alphabet is some permutation 
# of lowercase letters.

# Given an array of words A of size N written in the alien language, 
# and the order of the alphabet denoted by string B of size 26, return 1 
# if and only if the given words are sorted lexicographically in this alien 
# language else, return 0.

def solve(A, B):
        hashmap_pos=dict()
        #take the position of all lower case letters in the string of length 26, i.e.:-B
        for i in range(26):
            if B[i] not in hashmap_pos:
                hashmap_pos[B[i]]=i
        
        
        # we check on each words word1 and word2. we check their lexicographic cronology of querylist:A
        # according to the positions in the alphabets' order in B
        
        for i in range(1,len(A)):
            word1=A[i-1]
            word2=A[i]
            # keep greater as False
            greater =False
            pos=0
            # we check for each position till one of then reaches the end of its length
            while (pos <len(word1)) and (pos<len(word2)):
                # if position of word1 is greater than word2 we return 0
                if hashmap_pos[word1[pos]]>hashmap_pos[word2[pos]]:
                    #flag=0
                    return 0
                # if position same we go to next position
                elif hashmap_pos[word1[pos]]==hashmap_pos[word2[pos]]:
                    pos+=1
                #else we break and go for next words in the query
                else:
                    greater = True
                    break
            # for situation like "none" and "no" like words 
            if not greater and len(word1)>len(word2):
                return 0
        
        return 1
    
#print()