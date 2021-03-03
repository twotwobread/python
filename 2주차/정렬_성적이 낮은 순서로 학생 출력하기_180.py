# 성적이 낮은 순서로 학생 출력
# 입력 : 학생의 수 N (1 <= N <= 100,000)
#        학생이름, 학생성적 a,b ( 1 <= a,b <= 100)

n = int(input())
students = []
for i in range(n):
    a,b = map(str, input().split()) # 학생 정보
    students.append([a, int(b)]) # 리스트 저장

students = sorted(students)
for i in range(n):
    print(students[i][0], end=' ')

