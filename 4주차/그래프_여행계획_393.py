# 여행 계획
# N개의 여행지가 있고 각 여행지는 1~N번까지의 번호로 구분
# 또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다. 이때 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미
# 수영이는 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 한다. 예를 들어 N=5이고, 다음과 같이 도로의 정보가 주어졌다고 가정하자
# 1번 - 2번
# 1번 - 4번
# 1번 - 5번
# 2번 - 3번
# 2번 - 4번
# 만약 수영이의 여행 계획이 2 -> 3-> 4-> 3 이라고 하자 이 경우 2 -> 3 -> 2 -> 4 -> 2 -> 3 의 순서로 여행지를 방문하면, 여행 계획을 따를 수 있다.
# 여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 한울이의 여행 계획이 가능한지의 여부를 판별하는 프로그램 작성
# 입력조건: 여행지 수 N, 도시의 수 M ( 1 <= N, M <= 500 )
#                N개의 줄에 걸쳐 N x M 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어짐. 그 값이 1이라면 서로 연결되었다는 의미, 0이면 서로 연결 X
#                마지막 줄 수영이의 여행 계획에 포함된ㄴ 여행지의 번호들이 주어짐
# 출력조건: 한울이의 여행 계획이 가능하다면 YES, 불가능하다면 NO

def find_gil(graph, s, e, visited):
    result = False
    count = 0
    visited[s] = True
    for i in graph[s]:
        if i != 1:
            count+=1
            continue
        if visited[e] == True: # e에 도달하면 True를 반환하고 거기서부터 돌아와서 result=True를 넣어줌
            return True
        if not visited[count]: # 들어갔던 곳을 다시 안가기 위해서
            result = find_gil(graph, count, e, visited)
        count+=1
    # visited[e]가 True가 되어서 안에서 True 한걸 result로 받아서 표현
    if result==False: # visited[e]가 False면 False
        return False
    else:
        return True
            
        

n, m = map(int, input().split()) # 여행지 수, 내가 계획한 여행지의 수

graph = [[0]*(n+1) for _ in range(n+1)]# 도로의 정보를 2차원 배열을 이용해서 받아온다.

for i in range(1, n+1):
    g = list(map(int, input().split())) 
    graph[i] = g
    graph[i].insert(0, 0)


plan = list(map(int, input().split())) # 내가 여행할 여행지 계획

for i in range(len(plan)-1): # 2->3->4->3 이면 2->3, 3->4, 4->3을 검사한다.
    visited = [False]*(n+1)
    check = find_gil(graph, plan[i], plan[i+1], visited)
    if check == False: # check가 False면 도착할 수 없음
        print("NO")
        check = 100
        break
    print()
if check != 100:
    print("YES")
