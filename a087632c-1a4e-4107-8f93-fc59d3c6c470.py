import sys
sys.setrecursionlimit(int(1e7))

n = int(input())
a = list(map(int, input().split()))

tree = [0 for i in range(100005 * 4)]

def initTree(s, e, node):
    if s == e:
        tree[node] = [a[s], s]
        return tree[node]
    
    mid = (s + e) // 2
    left = initTree(s, mid, node * 2)
    right = initTree(mid + 1, e, node * 2 + 1)
    if left[0] < right[0]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]
    
def getMin(s, e, x, y, node):
    if e < x or y < s:
        return [987654321, -1]
    if x <= s and e <= y:
        return tree[node]
    
    mid = (s + e) // 2
    left = getMin(s, mid, x, y, node * 2)
    right = getMin(mid + 1, e, x, y, node * 2 + 1)
    
    if left[0] < right[0]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]

ans = 0
initTree(0, n - 1, 1)

def dfs(s, e):
    global ans
    if s >= e:
        return
    
    m = getMin(0, n - 1, s, e, 1)
    ans = max(ans, (e - s + 1) * m[0])
    
    mid = m[1]
    
    dfs(s, mid - 1)
    dfs(mid + 1, e)

dfs(0, n - 1)
print(ans)
    
