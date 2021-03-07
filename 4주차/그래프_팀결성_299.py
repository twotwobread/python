# 팀 결성
# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다.처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재한다. 이때 선생님은 '팀합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
# 팀 합치기 연산은 두팀을 합치는 연산이다. 같은 팀여부 확인 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
# 선생님이 M개의 연산을 수행할 수 있을때, 같은 팀 여부 확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.
# 입력조건: N, M ( 1<=N, M <=100,000 )
#                다음 M의 줄에는 각각의 연산이 주어진다. 팀 합치기 연산은 0 a b 형태로 주어진다. a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미
#                같은 팀 합치기 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속한지를 확인하는 연산
#                a, b <= N
# 출력조건:  같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES or NO 로 결과 출력

import sys
import heapq

def find_parent(parent, x): # 루트인 부모를 찾는 함수
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 팀을 합치기 위한 함수 먼저 루트인 부모를 찾고 큰지 안큰지를 확인하고 더 작은게 부모가 되는 방식
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

def union_check(parent, a, b): # 같은 팀인지 확인하기 위해서 루트인 부모를 찾고 같은지 확인
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        print("YES")
    else:
        print("NO")

n, m = map(int, sys.stdin.readline().split()) # 노드 개수와 연산 횟수
parent = [0]*(n+1)

for i in range(0, n+1): # 팀이 0~N개 인것 전부 개별적이라서 전부 루트임.
    parent[i] = i

for i in range(m):
    kind, a, b = map(int, sys.stdin.readline().split()) # 연산 정보
    if kind == 0:
        union_parent(parent, a, b)
    else:
        union_check(parent, a, b)
        

    
