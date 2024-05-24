def findPeople(name, peopleName):
    def starts_with(prefix, string):
        return string[:len(prefix)] == prefix
        
    start, end = -1, -1
    l, r = 0, len(peopleName) - 1
    m = 0
    
    while l <= r:
        print('loop')
        m = (l + r) // 2
        
        if starts_with(name, peopleName[m]) and (m == 0 or not starts_with(name, peopleName[m - 1])):
            start = m
            break
        elif peopleName[m] < name:
            l = m + 1
        else:
            r = m - 1
    
    if start == -1:
        return 0
    
    l, r = 0, len(peopleName) - 1
    m = 0 
    while l <= r:
        print('loop')
        m = (l + r) // 2
        
        if starts_with(name, peopleName[m]) and (m == len(peopleName) - 1 or not starts_with(name, peopleName[m + 1])):
            end = m
            break
        elif peopleName[m] > name:
            r = m - 1
        else:
            l = m + 1
            
    if end == -1:
        return 0
    
    result = end - start + 1
    return result
