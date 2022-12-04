def encryptionValidity(instructionCount, validityPeriod, keys):
    # Write your code here
    result = [0,0]
    mx_divis = -1
    keys.sort(reverse=True)
    for i in range(0, len(keys)):
        i_ele = keys[i]
        count = 1
        for j in range(i+1, len(keys)):
            j_ele = keys[j]
            if i_ele%j_ele == 0:
                count += 1
        mx_divis = max(mx_divis, count)
        print(mx_divis)
        if mx_divis >= (len(keys)-i+1):
            break
    result[1] = mx_divis*100000
    p = list(str(instructionCount)).count('0')
    p += list(str(validityPeriod)).count('0')
    
    if p > 5:
        result[0] = 1
    elif((instructionCount*validityPeriod)-result[1] >= 0):
        result[0] = 1
    return result

print(encryptionValidity(100,1000,[2, 4]))