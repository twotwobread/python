# 도현이네 반 학생 N명의 이름과 국어, 영어 ,수학 점수가 주어짐
# 다음과 같은 조건으로 정렬해라
# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서
# 3. 국겅, 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 이름 사전 순으로 증가하는 순서(대문자가 소문자 앞에 온다.)
# 입력 조건 : 반의 학생 수 N ( 1<=N<=100,000)
#             이름, 국어, 영어, 수학 점수가 공백으로 구분
#             점수는 1보다 크거나 같고, 100보다 작거나 같은 자연수
#             이름은 최대 10자리
# 출력 조건 : 학생이름을 출력
# 계수 정렬 써야겠다.
from bisect import bisect_left, bisect_right
"""
def quickSort(array, start, end):
    if start>=end:
        return
    pivot = start
    left=start+1
    right = end
    while left <= right:
        while left <= end and array[left][1] <= array[pivot][1]:
            left+=1
        while right > start and array[right][1] >= array[pivot][1]:
            right-=1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quickSort(array, start, right-1)
    quickSort(array, right+1, end)
"""

def setting_korean(data):
    return data[1]
"""
def printList(list, condition):
    for i in list:
        left = bisect_left(list, i[condition])
"""         

n = 12
"""
list=[["Junkyu", 50, 60, 100],
    ["Sangkeun", 80, 60, 50],
    ["Sunyoung", 80, 70, 100],
    ["Soong" ,50 ,60 ,90],
    ["Haebin", 50 ,60 ,100],
    ["Kangsoo" ,60 ,80 ,100],
    ["Donghyuk", 80, 60, 100],
    ["Sei" ,70 ,70 ,70],
    ["Wonseob", 70, 70, 90],
    ["Sanghyun", 70, 70, 80],
    ["nsj", 80, 80, 80],
    ["Taewhan", 50, 60, 90]]
"""
list = [10,20,30, 80, 80, 80]
condition = 1
#quickSort(list, 0, len(list)-1)
#sorted_list = sorted(list, key=setting_korean, reverse=True)
sorted_list = sorted(list, reverse=True)
left = bisect_left(sorted_list, 80)
right = bisect_right(sorted_list, 80)
print(left, right)
print(sorted_list)

