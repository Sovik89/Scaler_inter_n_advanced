def lcm(a, b) :
        def gcd(a, b) :
            if b == 0 :
                return a
            return gcd(b, a % b)
        return a * b // gcd(a, b)

def solve(A, B, C):
        l = min(B, C)
        r = min(B, C) * A
        LCM = lcm(B, C)
        while l <= r :
            mid = (l + r) // 2
            cf = mid // B + mid // C - mid // LCM
            if cf < A :
                l = mid + 1
            elif cf > A :
                r = mid - 1
            else :
                ans = mid
                r = mid - 1
        return ans % 1000000007
    
    


print(solve(4,2,3))