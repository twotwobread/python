def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side) 

n,k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = quick_sort(a)
sorted_b = quick_sort(b)

for i in range(k):
    if sorted_a[i] < sorted_b[n-1-i]:
        sorted_a[i], sorted_b[n-1-i] = sorted_b[n-1-i], sorted_a[i]
    else:
        break

print(sum(sorted_a))





