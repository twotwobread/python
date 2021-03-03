from bisect import bisect_right, bisect_left
def cutTteokbokki(length_array, cmp_array, target, start, end):
    if start > end:
        return False
    mid = (start + end)//2
    location = bisect_right(cmp_array, mid)
    s = sum(cmp_array[location:end+1])-(len(cmp_array[location:end+1])*length_array[mid])
    if s == target:
        return length_array[mid]
    elif s < target:
        return cutTteokbokki(length_array, cmp_array, target, start, mid-1)
    else:
        return cutTteokbokki(length_array, cmp_array, target, mid+1, end)
    



n, m = map(int, input().split())
h = list(map(int, input().split()))
h = sorted(h); max_cm = h[len(h)-1]
all_length_list = [x for x in range(max_cm+1)]
result = cutTteokbokki(all_length_list, h, m, 0, len(all_length_list)-1)
print(result)
         
