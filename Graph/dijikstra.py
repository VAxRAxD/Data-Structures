from collections import deque
class PriorityQueue:
    def __init__(self):
        self.buffer=deque()
    def push(self,dist,node):
        self.buffer.appendleft([dist,node])
    def pop(self):
        min=0
        for i in range(1,len(self.buffer)):
            if self.buffer[i][0]<self.buffer[min][0]:
                min=i
        item=self.buffer[min]
        del self.buffer[min]
        return item

class Graph:
	def __init__(self,nodes,adj):
		self.nodes=nodes
		self.adj=adj

n=4
m=[[1,2,5],[1,4,40],[2,3,10],[3,4,10]]
adj =[[] for _ in range(n)]
for edge in m:
    i,j,weight=map(int,edge)
    adj[i-1].append([j,weight])