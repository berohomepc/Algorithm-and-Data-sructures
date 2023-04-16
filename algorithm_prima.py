from queue import PriorityQueue

q = PriorityQueue()
n, m = map(int, input().split())
G = []
for i in range(n):
	G.append(list())

for i in range(m):
    start, end, weight = map(int, input().split())
    G[start-1].append((weight, end-1))
    G[end-1].append((weight, start-1))

key = [int(1e9)] * n

# print(G)
used = []
def primFindMST():
	key[0] = 0
	for i in range(0, n):
		q.put((key[i], i))
	
	while not q.empty():
		v = q.get()[1]
		if v in used:
			continue
		used.append(v)

		for a, u in G[v]:
			if not u in used and key[u] > a:
				key[u] = a
				q.put((key[u], u))

primFindMST()
print(sum(key))
