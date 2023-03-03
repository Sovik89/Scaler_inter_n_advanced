def romanToInt( s: str) -> int:
        hash_map={'I':[0,1], 'V':[1,5],'X':[2,10],'L':[3,50],'C':[4,100],'D':[5,500],'M':[6,1000]}
        
        n=len(s)
        out=0
        original_index=hash_map[s[n-1]][0]
        for i in range(n-1,-1,-1):
            current_index=hash_map[s[i]][0]            
            if current_index == original_index:
                out+=hash_map[s[i]][1]
            elif current_index<original_index:
                out-=hash_map[s[i]][1]
                original_index=hash_map[s[i]][0]
            else:
                out+=hash_map[s[i]][1]
                original_index=hash_map[s[i]][0]
                
        return out
    

print(romanToInt("MCMXCIV"))
            
            