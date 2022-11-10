def LargButMinFreq(arr):
    #code here
    #[2,2,5,5,1]
    #[0,0,0,0,0]
    #[1,2,0,0,2]
    ma = find_max(arr)                  #Time O[N]
    c = [0 for i in range(ma)]
    for i in arr:                       #Time O[N]
        occr = c[i-1] + 1
        c[i-1] = occr
    mi = find_min(c)                    #Time O[M]
    for i in range(len(c)-1, -1, -1):   #Time O[M]
        if c[i] == mi:
            return i+1

def find_max(arr):                  #Time O[N]
    m = None
    for i in arr:
        if(m==None or m < i):
            m = i
    return m

def find_min(arr):                  #Time O[M]
    m = None
    for i in arr:
        if(m==None or m > i):
            m = i
    return m
LargButMinFreq([2,2,5,50,1])
