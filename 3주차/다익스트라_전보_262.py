# N개의 도시가 있다. X->Y로 전보를 보내기 위해선 간선이 있어야한다. 간선을 거쳐 메시지를 보낼 때는 일정 시간이 소요
# C에서 상황 발생 최대한 많은 도시로 메시지를 보내고자 한다면 간선을 거쳐서 최대한 많이 퍼져나갈 것
# 각 도시의 번호와 간선이 설치되어 있는 정보가 주어졌을 때, C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 모두 메시지를 받는 데까지 걸리는 시간은 얼마인가?
# 입력 조건: 노드 개수 N, 간선 개수 M, 메시지를 보내고자 하는 도시 C ( 1<=N<=30,000, 1<=M<=200,000, 1<=C<=N )
#            간선에 대한 정보 X, Y, Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미
#            ( 1<=X,Y<=N, 1<=Z<=1,000 )
# 출력 조건: C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간
# 노드 개수가 너무 많아서 플로이드 워셜은 쓰기 어려움
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m): # 간선을 graph에 넣어줌
    x, y, z = map(int, input().split())
    graph[x].append((y,z)) # x에서 y로 가는 소요시간이 z

def dijkstra(c):
    q = [] 
    heapq.heappush(q,(0, c))
    distance[c] = 0
    while q: # 큐가 비어있지 않을때
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
time = 0
for i in distance:
    if i == INF:
        continue
    count +=1
    time = max(time, i)
print(count-1, time)
