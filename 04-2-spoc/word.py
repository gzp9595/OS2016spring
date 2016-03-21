memory = ['e', 'd', 'a']
tmp = ['e', 'd', 'a']
addr = ['c', 'c', 'd', 'b', 'c', 'e', 'c', 'e', 'a', 'd']
t = 4
for i in addr:
    if not i in memory:
        print i+"\tmiss"
        memory.append(i)
    else:
        print i+"\thit"
    if (len(tmp) == t):
        tmp = tmp[1:]
        tmp.append(i)
    else:
        tmp.append(i)
    for i in memory:
        if not i in tmp:
            print i+"\tfilter"
            memory.remove(i)
            


