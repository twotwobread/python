# 고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미
# ex) a = {-15, -4, 2, 8, 13} a[2] = 2 이므로 고정점은 2이다.
# 오름차순으로 입력이 되고 이 수열에 고정점이 있다면 고정점 출력 없으면 -1 출력
# 시간 복잡도 log N 으로 풀것
# 입력 조건 : 첫째 줄에 N ( 1 <= N <= 1,000,000 )
#             둘째 줄 N개의 원소가 정수 형태로 공백으로 구분되어 입력 ( -10^9 <= 각 원소의 값 <= 10^9 )
# 출력 조건 : 고정점 출력 없으면 -1 출력

def binarySearch_FixedPoint(array, start, end):
    if start > end:
        return -1

    mid = (end + start)//2
    if array[mid] < mid:
        return binarySearch_FixedPoint(array, mid+1, end)
    elif array[mid] > mid:
        return binarySearch_FixedPoint(array, start, mid-1)
    else:
        return mid

n = 7
L = [-15, -4, 3, 8, 9, 13, 15]

mid = binarySearch_FixedPoint(L, 0, len(L)-1)
print(mid)
