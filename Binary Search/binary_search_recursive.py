import math

arr = [4,8,10,15,18,21,24,27,19,33,37,34,37,41,43]

def binary_search(l,h,ele):
    mid = math.floor((l+h)/2)
    if ele == arr[mid]:
        return mid
    elif ele < arr[mid]:
        h = mid -1
        return binary_search(l,h,ele)
    else:
        l = mid + 1
        return binary_search(l,h,ele)

l = 0
h = len(arr) - 1
ele = 41
print(binary_search(l,h,ele))
