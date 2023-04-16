edges = []
n, m = map(int, input().split())

for i in range(m):
    start, end, weight = map(int, input().split())
    edges.append([weight, start-1, end-1])
    
edges.sort()

comp = [i for i in range(n)]

ans = 0
for weight, start, end in edges:
    if comp[start] != comp[end]:
        ans += weight
        a = comp[start]
        b = comp[end]
        for i in range(n):
            if comp[i] == b:
                comp[i] = a
print(ans)