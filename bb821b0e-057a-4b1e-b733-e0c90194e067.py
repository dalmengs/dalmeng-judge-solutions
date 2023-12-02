n = int(input())

synonym = {}
summary = []

for _ in range(n):
    q = input().split()
    
    k = int(q[0])
    for j in q[1:]:
        synonym[j.lower()] = len(summary)
    
    t = int(input())
    temp = []
    for __ in range(t):
        temp.append(input())
    summary.append(temp)

t = int(input())
for _ in range(t):
    q = input().split()
    
    k = int(q[0])
    if k == 1:
        x, y = q[1].lower(), q[2].lower()
        synonym[y] = synonym[x]
    elif k == 2:
        x, y = q[1].lower(), " ".join(q[2:])
        summary[synonym[x]].append(y)
    else:
        for i in summary[synonym[q[1].lower()]]:
            print(i)
