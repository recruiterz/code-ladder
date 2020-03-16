def twoStrings(s1, s2):
    d = set(s1)
    
    for s in s2:
        if s in d:
            return 'YES'
    return 'NO'
