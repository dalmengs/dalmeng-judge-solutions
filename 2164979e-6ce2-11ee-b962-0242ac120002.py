def decimalToHex(n, base = 16):
    ret = []
        
    while n:
        ret.append(n % base)
        n //= base
        
    return "".join(reversed(list(map(str, ret))))

n = int(input())
s = decimalToHex(n)
n = len(s)

ans = 0
for i in range(n):
    ans += 16**i * int(s[-(i + 1)])

print(ans)
