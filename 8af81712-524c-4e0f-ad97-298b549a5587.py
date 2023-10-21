s = input()
x = input()
y = input()

# Find 기능 
cnt = 0
for i in range(len(s)):
    if i + len(x) > len(s):
        break
    z = s[i:(i+len(x))]
    if x == z:
        cnt += 1
if cnt == 0:
    print("No Results")
else:
    print("{} Found".format(cnt))

# Replace 기능 
res = ""
i = 0
while i < len(s):
    if i + len(x) > len(s):
        res += s[i]
        i += 1
        continue
    
    z = s[i:(i+len(x))]
    if x == z:
        res += y
        i += len(x)
    else:
        res += s[i]
        i += 1

print(res)
