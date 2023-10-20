n = int(input())
a = list(map(int, input().split()))

ans = 0

def memset(x):
    return [0 for _ in range(x)]

for i in range(n):
    arr = memset(n)
    cnt = 1
    now = i
    while True:
        if arr[now] != 0: # 뫼비우스의 발판을 찾은 경우 
            ans = max(ans, cnt - arr[now])
            break
        else:
            arr[now] = cnt # 발판 방문 처리 
        
        nxt = now + a[now] # 다음 발판 위치 
        if nxt < 0 or nxt >= n: # 발판을 벗어나는 경우 
            break
        now = nxt # 현재 발판이 다음 발판이 된다 
        cnt += 1

print(ans)
