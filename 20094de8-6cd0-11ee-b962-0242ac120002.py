def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)
n = len(s)

def solve(idx):
    if idx == n:
        return 1
        
    ret = solve(idx + 1)
    if idx + 1 < n and s[idx] == "1" and s[idx + 1] in "012345":
        ret += solve(idx + 2)
    
    return ret

print(solve(0))
