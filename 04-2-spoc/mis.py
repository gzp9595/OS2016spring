import random

ACCESS_COUNT = 20
WINDOW_SIZE = 2
PAGE_NUM = 6
MEM_SIZE = 4

accessList = [random.randint(0,PAGE_NUM) for i in xrange(ACCESS_COUNT)]
print accessList
D = {}
last = -1
for current in xrange(ACCESS_COUNT):
    idx = accessList[current]
    if idx in D:
        D[idx] = current
        print "access", idx, "hit"
    else:
        if current - last <= WINDOW_SIZE:
            D[idx] = current
            print "access", idx, "miss", "load", D.keys()
            last = current
            if (len(D) > MEM_SIZE):
                tmp = D.items()
                tmp.sort(lambda x, y: x[1] - y[1])
                D = dict(tmp[1:])
        else:
            tmp = []
            for i in D.items():
                if(i[1] >= last):
                    tmp.append(i)
            D = {}
            for i in tmp:
                D[i[0]] = 0
            D[idx] = current
            print "access", idx, "miss", "filter & load", D.keys()
            last = current
