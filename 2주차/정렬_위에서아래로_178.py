# 위에서 아래로
# 입력 : 수열에 속해 있는 수의 개수 N(1<=N<=50)
#        수열에 속한 N개의 수 M(1 <= M <= 100,000)

n = int(input()) # 수열에 속한 수의 개수
m = []
for i in range(n):
    m.append(int(input())) # 수열에 속한 숫자
m = sorted(m, reverse=True)
for j in range(n):
    print(m[j], end=" ")

