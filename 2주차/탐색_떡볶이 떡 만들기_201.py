#떡볶이 떡 만들기
# 수영이네 떡볶이 가게 떡의 길이는 일정하지 않다. 대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줌.
# 절단기에 높이 (H)를 지정하면 줄지어진 떡을 한 번에 절단함. 높이가 H보다 길면 H위의 길이가 잘리고 짧으면 안짤림.
# 손놈이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
# 입력 조건: 떡의 개수 N, 요청한 떡의 길이 M ( 1<=N<=1,000,000, 1<=M<=2,000,000,000)
#            떡의 개별 높이 , 떡 높이의 총합은 항상 M이상 (높이는 10억보다 작거나 같은 양의 정수 또는 0이다.)
# 출력 조건: 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수있는 높이의 최댓값을 출력한다.

# 4 6
# 19 15 10 17     15
# 위의 경우 6 이런식으로 나오게 하는 법을 못풀겠어서
# 그냥 내가 가지고 있는 길이로 풀게 했음.
# 근데 저런식으로 풀려면 최대길이가 19 면 0~19가 있는 리스트하나로 이진탐색하듯 하면 되겠노 개지리노


def cutTteokbokki(array, target, start, end, s):
    global check # 내가 가지고 있는 길이 중에 없을경우
    if start>end:
        return check
    mid = (start+end)//2
    temp = sum(array[mid:end+1])-(len(array[mid:end+1])*array[mid]) # mid에서 끝까지 mid 값만큼 잘라서 더함
    s = s+temp # 이전에 잘랐던 길이들이랑 더함
    if  s > target:# 요청 길이보다 길다.
        check = array[mid] # 요청 길이를 포함하는 최솟값 체크
        s = 0; # 요청 길이 보다 더 길게 잘랐으면 굳이 이전에 잘랐던 길이가 필요없다.
        return cutTteokbokki(array, target, mid+1, end, s) # 더 긴 길이로 잘라서 잘리는 길이는 짧아진다.
    elif s < target: # 요청 길이보다 짧다.
        s += (len(array[mid:end])*(array[mid]-array[mid-1])) # 그러면 이전에 짤랐던 길이보다 더 짧은 길이로 짤라야하니까 잘리는 길이는 늘어나서 요렇게 
        return cutTteokbokki(array, target, start, mid-1, s)
    else: # 내가 가지고 있는 길이 중에 존재해
        return array[mid]
    
n, m = map(int, input().split()) # 떡의 개수, 떡의 길이
h = list(map(int, input().split())) # 떡의 개별 높이
h = sorted(h)

count, check = 0, 0
result = cutTteokbokki(h, m, 0, n-1, 0)
print(result)



