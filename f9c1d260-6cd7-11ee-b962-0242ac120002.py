def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)
n = len(s)

dp = [0 for i in range(n)]

def solve(idx):
    if idx == n:
        return 1
        
    if dp[idx]:
        return dp[idx]
    
    ret = solve(idx + 1)
    if idx + 1 < n and s[idx] == "1" and s[idx + 1] in "012345":
        ret += solve(idx + 2)
        
    dp[idx] = ret
    return ret

print(solve(0))
