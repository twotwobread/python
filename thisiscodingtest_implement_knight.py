#8x8 좌표 평면
#나이트는 L자 형태로만 이동 가능, 정원 밖은 불가
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 나이트의 위치가 주어지면 이동할 수 있는 경우의 수 출력하기
# row = 1,2,3,4,5,6,7,8
# col = a,b,c,d,e,f,g,h

count = 0
str_ex = 'a1'
x, y = str_ex[0], int(str_ex[1])

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['L', 'R', 'U', 'D'] # 동서남북 한칸씩 움직이는 거
move_type = ['UL', 'UR', 'LU', 'RU', 'DL', 'DR', 'LD', 'RD']
# 나이트가 움직일 수 있는 모든 경우의 수

for i in range(8):
    m = move_type[i]
    p1 = move.index(m[0]) #첫번째 문자열의 move에서의 위치
    nx = ord(x) + dx[p1]
    ny = y + dy[p1]
    
    p2 = move.index(m[1]) #두번째 문자열의 move에서의 위치
    for j in range(2):
        nx += dx[p2]
        ny += dy[p2]
    # 좌표 평면 상에 있는지 알아보는것
    if (nx < ord('a')) or (nx>ord('h')) or (ny<1) or (ny>8):
        continue
    else:
        count+=1
print(count)
