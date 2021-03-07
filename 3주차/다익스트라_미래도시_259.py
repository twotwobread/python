# 미래 도시
# 현재 1번 회사에 위치 X번 회사에 방문해 물건을 판매하고자 한다.
# 양방향으로 이동, 도로에서는 1만큼의 사간으로 이동
# 1번회사에서 K번 회사를 방문한 뒤에 X번 회사에 도착하기 위한 최소 시간을 계산
# ex) (1,2), (1,3), (1,4), (2,4), (3,4), (3,5), (4,5) / N=5, X=4, K=5  도로는 7개
# 최종 루트는 1-3-5-4 로 설정하면 3만큼의 시간으로 이동하고 소개팅 참석 가능
# 입력 조건 : (1<=N,M<=100)
#            두 회사의 번호가 주어짐
#            X와 K가 주어짐(1<=K<=100)
# 출력 조건 : 최소 이동 시간을 출력
#            도달 불가능하면 -1 출력
import heapq
import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().rstrip().split()) # 노드랑 간선 수

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input().split()) # 도착, 들릴 곳

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = graph[1][k] + graph[k][x] # 1번에서 k를 거쳐서 x까지 가는 최소 시간

if result >= INF:
    print("-1")
else:
    print(result)
    
