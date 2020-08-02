import math
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        MOD = 10**9 + 7
        L = A / math.gcd(A,B) * B
        def magic_below_x(x):
            return x / A + x / B - x / L
        lo = 0
        hi = N * min(A, B)
        while lo < hi:
            mi = (lo + hi) / 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return int(lo % MOD)
val=Solution()
n,a,b=map(int,input().split())
print(val.nthMagicalNumber(n,a,b))
