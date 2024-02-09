n = int(input())
a = [0] + list(map(int, input().split())) + [0]
s = [0]
ans = 0
for i in range(1, len(a)):
    while len(s) and a[s[-1]] > a[i]:
        last = s.pop()
        ans = max(ans, (i - s[-1] - 1) * a[last])
    s.append(i)
print(ans)
