# 부품 찾기
# 수영이네 전자 매장에는 N개의 부품이 존재함 (각 부품에는 고유번호 존재)
# 손놈이 와서 M개 부품을 달라고 요구 확인해서 견적서 찾아주자
# 입력 조건 :   N ( 1<=N<=1,000,000)
#               N개의 정수 ( 1<=정수<=1,000,000 )
#               M ( 1<=M<=100,000)
#               M개의 정수 ( 1<=정수<=1,000,000 )
# 출력 : 각 부품이 존재하면 yes, 없으면 no
# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes
import sys

def bin_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end)//2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return bin_search(array, target, mid+1, end)
    else:
        return bin_search(array, target, start, mid-1)
        

n = int(input())
n_array = list(map(int, input().split()))
m = int(input())
m_array = list(map(int, input().split()))
n_array = sorted(n_array)

for i in m_array:
    x = bin_search(n_array, i, 0, len(n_array)-1)
    if x == True:
        print("yes", end=" ")
    elif x == False:
        print("no", end=" ")


