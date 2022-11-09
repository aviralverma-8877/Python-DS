def findFrequency (arr, n, x):
    # Your Code Here
    #[2,5,8,2,6,2,7,2,4,9]
    m = find_greatest(arr)
    c = [0 for i in range(m)]
    for i in arr:
        c[i] += 1
    return c[x]

def find_greatest(arr):         #Time O(n)
    m = None
    for i in arr:
        if m == None or m < i:
            m = i
    return m

findFrequency([1,1,1,1,1,1,1], 7 ,1)