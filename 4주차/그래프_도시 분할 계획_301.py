# 도시 분할 계획
# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 그 길마다 길을 유지하는데 드는 유지비가 있다.
# 마을 이장은 마을을 2개의 마을로 분할할 계획이다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.
#길이 너무 많다는 생각을 하게 되었다. 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다. 이장은 조건을 만족하도록 길을 없애 돈을 덜 들게 하고 싶다.
# 입력조건: 집의 개수 N, 길의 개수 M ( 2 <= N <= 100,000, 1<= M <= 1,000,000 )
#                M줄에 걸쳐 길의 정보가 주어짐  a, b ,c ( a번 집과 b번 집을 연결하는 길의 유지비가 c( 1<= c <= 1,000 )
# 출력조건: 길을 없애고 남은 유지비 합의 최솟값
# 사이클 되는 부분이 없어야함
# 그래서 최소 신장 트리 크루스칼 알고리즘을 써야할듯

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x<y:
        parent[y]= x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [0]*(n+1)

edges, result = [], 0

for i in range(1, n+1):
    parent[i] = i

for  _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for e in edges:
    c, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        max_price = c

print(result-max_price)
