def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)
n = len(s)

dp = [1 for i in range(n)]

for i in range(1, n):
    dp[i] = dp[i - 1]
    if s[i - 1] == "1" and s[i] in "012345":
        dp[i] += (dp[i - 2] if i >= 2 else 1)

print(dp[n - 1])
    
    

