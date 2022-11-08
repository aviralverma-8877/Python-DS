import math

arr = [4,8,10,15,18,21,24,27,19,33,37,34,37,41,43]

def binary_search(ele):
    l = 0
    h = len(arr)-1
    while l<=h:
        mid = math.floor((l+h)/2)
        if ele == arr[mid]:
            return mid
        elif ele < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return False


print(binary_search(18))