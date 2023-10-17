n = int(input())

w = [0, 5]
h = [0, 3]
for i in range(10):
    w.append(w[-1] * 2 - 1)
    h.append(h[-1] * 2 - 1)

arr = [[' ' for i in range(w[n])] for j in range(h[n])]
def makeTree(size, x, y):
    if size == 0:
        return
    
    for i in range(w[size]):
        arr[y][x + i] = '*'
    for i in range(h[size]):
        arr[y - i][x + i] = '*'
    for i in range(h[size]):
        arr[y - i][x + w[size] - 1 - i] = '*'
    
    makeTree(size - 1, x, y)
    makeTree(size - 1, x + w[size - 1] - 1, y)
    makeTree(size - 1, x + (w[size - 1] // 2), y - (h[size - 1] - 1))
    
makeTree(n, 0, h[n] - 1)
for i in arr:
    print("".join(i).rstrip())
