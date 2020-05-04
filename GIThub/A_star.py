import queue
INF=int(1e9)
MAX=20
class Node:
	def __init__(self, id, dist, f):
		self.id=id
		self.dist=dist
		self.f=f
	def __lt__(self, other):
		return self.f<=other.f
def A_star(s, t):
	S=d[s]
	T=d[t]
	pq=queue.PriorityQueue()
	pq.put(Node(S, 0, h[S]))
	while 1:
		top=pq.get()
		u=top.id
		if u==T: break
		w=top.dist
		for nb in graph[u]:
			if w + nb.dist<dist[nb.id]:
				dist[nb.id]=w+nb.dist
				path[nb.id]=u
				pq.put(Node(nb.id, dist[nb.id], dist[nb.id]+h[nb.id]))

def printpath(s, t):
	key_list=list(d.keys())
	val_list=list(d.values())
	S=d[s]
	T=d[t]
	temp=path[T]
	a=[T]
	while temp!=S:
		a.append(temp)
		temp=path[temp]
	a.append(S)
	for i in range(len(a)):
		a[i]=key_list[val_list.index(a[i])]
	print(a[::-1])

h=[]
d={}
with open('h.txt') as file:
	i=0
	for line in file:
		l=line.split()
		d[l[0]]=i
		i+=1
		h.append(int(l[1]))

graph=[[] for _ in range(MAX)]
dist=[INF for _ in range(MAX)]
path=[-1 for _ in range(MAX)]

with open('g.txt') as file:
	for line in file:
		l=line.split()
		u=d[l[0]]
		v=d[l[1]]
		w=int(l[2])
		graph[u].append(Node(v, w, 0))
		graph[v].append(Node(v, w, 0))

A_star('Arad', 'Bucharest')
printpath('Arad', 'Bucharest')
print(dist[d['Bucharest']])

