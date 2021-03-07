#커리큘럼
# 선수강의를 먼저 들어야만 해당 가의를 들으 수 있다.
# 총 N개의 강의를 듣고자 하는데 모든 강의는 1번부터 N번까지의 번호를 가진다. 또한 동시에 여러개의 강의를
# 들을 수 있다. 예를 들어서 N=3일때, 3번 강의의 선수 강의로 1번과 2번 강의가 있고 1,2번은 선수과목 x
# 각 강의 시간은 1 = 30h, 2 = 20h, 3 = 40h 이라고 가정
# 이경우 3번 강의를 수강하기위한 최소 시간은 70시간이다.
# 입력조건 : N (1<=N<=500)
#           각 강의의 강의시간, 선수과목의 번호가 주어진다. (강의 시간 <= 100,000)
#           각 강의 번호는 1~N, 각 줄은 -1로 끝난다.
# 출력조건 : N개의 강의에 대한 최소 수강 시간
# 5
# 10 -1         10 ( 맨 앞이 강의 시간 ) 이게 1번 과목
# 10 1 -1       20 ( 강의 시간, 선수강 과목 번호) 이게 2번 과목=
# 4 1 -1        14 
# 4 3 1 -1      18 ( 강의 시간, 선수강 과목 번호 2개) 이게 4번 과목
# 3 3 -1        17

from collections import deque

n = int(input()) # 과목 개수

graph = [[] for i in range(n+1)] # 노드의 개수만큼 간선의 정보를 표현하는 거 초기화
time = [0]*(n+1)
result = [0]*(n+1)
for i in range(1, n+1): # 시간이랑 연결 노드를 따로 분리해서 정보 저장
    e = list(map(int,input().split()))
    t = e.pop(0)
    graph[i] = e
    time[i] = t

def myThink(now):
    if len(graph[now])==1: # 길이가 1인 노드를 만났을때 그 노드까지만 더하고 끝냄
        return time[now]
    for i in graph[now]:
        if i == -1: # 지금 현재 노드에서 -1을 만나면 끝내는 부분
            break
        temp=time[now]+myThink(i) # 계속 들어가서 더해주는 부분
        if temp > result[now]:
            result[now] = temp
        temp = 0
    return result[now]

for i in range(1, n+1):
    print(myThink(i))
            
            
        
    
# 이렇게 하면 1부터 출발해서 
#def topology_sort():
 #   q = deque()
  #  for i in range(1, n+1):
   #     if indegree[i] == 0:
    #        q.append(i)

    #while q:
     #   r = [] 
      #  now = q.popleft()
       # r.append(time[now])     # 결과 테이블에 수강 시간을 넣어주는 부분
       # for i in graph[now]:
        #    indegree[i] -= 1
         #   if indegree[i] == 0:
          #      q.append(i)
    
    
