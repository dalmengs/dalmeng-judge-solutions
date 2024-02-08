w, h = map(int, input().split())
k = int(input())
b = [0 for i in range(w + 2)]
for _ in range(k):
    t, n, x = map(int, input().split())
    if t == 1:
        b[x] += 1
        b[x + n] -= 1
    elif t == 2:
        b[x] += n
        b[x + 1] -= n
    elif t == 3:
        b[x] += 1
        b[x + n] -= 1
        b[x + n - 1] += n - 1
        b[x + n] -= n - 1
    elif t == 4:
        b[x] += 1
        b[x + n] -= 1
        b[x] += n - 1
        b[x + 1] -= n - 1
c = 0
for i in range(1, w + 1):
    c += b[i]
    if c > h:
        print(-1, end=" ")
    else:
        print(c, end=" ")
