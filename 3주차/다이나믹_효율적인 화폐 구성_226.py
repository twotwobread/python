# N가지 종류의 화폐를 이용해 M원을 만들때 최소한의 화폐 개수
# 입력 조건: N, M ( 1 <= N <= 100, 1 <= M <= 10,000)
#           이후 N개의 줄에는 각 화폐의 가치가 주어짐 화폐 가치는 10,000보다 작거나 같은 자연수
# 출력 조건:최소한의 화폐 개수 불가능하면 -1 출력
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
coin = []
for i in range(n):
    c = int(input())
    coin.append(c)
coin = sorted(coin)

d = [10001]*(m+1)

d[0] = 0
for i in range(n): # 화폐개수 
    for j in range(coin[i], m+1): # 최종 가격 어짜피 화폐 보다 더 밑에꺼는 계산 못하니까
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], d[j-coin[i]] + 1) # 개수로 표현

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    







