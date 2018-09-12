#Vocany Pitia
#CSCE 4430
#Assignment 1

final = []

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
def mot2(j):
    result = []
    if j == 0:
        result.append('leaf')
        final.append(result)
        #return result
    else:
        for v in mot2(j-1):
            result.append(tuple(('unary',v)))
            #print("Value of v", v)
            #print("Result in v", result)
        for k in range(0, j-1):
            for l in mot2(k):
                for r in mot2(j-2-k):
                    result.append(tuple(('binary',l,r)))
                    final.append(result)
                    #return result
    final.append(result)
    return result
def test(m):
    for n in range(m):
        list(map(print,list(mot(n))))

def test2(a):
    for x in range(a+1):
        print(mot2(x))
    #print(final)


if __name__ == '__main__':
    test(4)
    print("\n\n\n")
    test2(3)

