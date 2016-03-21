memory = ['e', 'd', 'a']
tmp = ['e', 'd', 'a']
addr = ['c', 'c', 'd', 'b', 'c', 'e', 'c', 'e', 'a', 'd']
t = 4
for i in addr:
    if not i in memory:
        print "access",i,"miss"
        memory.append(i)
    else:
        print "access",i,"hit"
    if (len(tmp) == t):
        tmp = tmp[1:]
        tmp.append(i)
    else:
        tmp.append(i)
    for i in memory:
        if not i in tmp:
            print "access",i,"filter"
            memory.remove(i)
            


