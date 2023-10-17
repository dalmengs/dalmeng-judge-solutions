def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)

def dfs(idx, k):
    if idx == -1:
        return 0
        
    ret = 0

    if idx - 1 >= -1:
        ret = dfs(idx - 1, k + 1) + 16**k * int(s[idx])
    if idx - 2 >= -1 and int(s[idx - 1] + s[idx]) < 16:
        ret = max(ret, dfs(idx - 2, k + 1) + 16**k * int(s[idx - 1] + s[idx]))
    return ret
        
print(dfs(len(s) - 1, 0))
