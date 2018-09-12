#Vocany Pitia
#CSCE 4430
#Assignment 1

#Motzkin Tree of Size n
def mot(n):
    if n == 0:
        yield 'leaf'
    else:
        for m in mot(n-1):
            yield ('unary',m)
        for k in range(0, n-1):
            for l in mot(k):
                for r in mot(n-2-k):
                    yield ('binary',l,r)

#Motzkin Tree of Size n
def mymot(j):
    result = []             #Holds the result for each tree of size N
    if j == 0:
        result.append('leaf')
    else:
        for v in mymot(j-1):
            result.append(tuple(('unary',v)))
        for k in range(0, j-1):
            for l in mymot(k):
                for r in mymot(j-2-k):
                    result.append(tuple(('binary',l,r)))
    return result

def test(m):
    for n in range(m):
        list(map(print,list(mot(n))))

#My test function to test mymot
def mytest(a):
    for x in range(a):
        for y in mymot(x):
            print(y)

if __name__ == '__main__':
    test(4)
    print("\n\n\n")
    mytest(4)

