from Util import *

def keygen():
    t = randomvector(n)
    sk = [1]
    for i in t:
        sk.append(i * -1)
    #sk = np.remainder(sk, q)
    B = randomarray(m, n)
    e = errorvec(m)

    b = np.dot(B, t.T) + e
    b = np.remainder(b, q)
    A = np.column_stack([b.T, B])
    #A = np.remainder(A, q)
    return A, sk

def enc(pk, u):
    R = errorarray(N, m)
    #A = u * np.identity(N, int) + bitdecomposearray(np.remainder(np.dot(R, pk), q))
    #print inversedecomposearray(A)
    #print len(A)
    #print bitdecomposearray(np.remainder(np.dot(R, pk), q))[0].size
    C = flattenarray(u * np.identity(N, int) + bitdecomposearray(np.remainder(np.dot(R, pk), q)))
    return C


def dec(sk, C):
    v = powerof2(sk)
    c = 0
    for i in range(0, len(v)):
        if v[i] <= q/2 and v[i] > q/4:
            c = i
            break
    x = np.dot(C[c], v) % q
    u = int(x/v[c]* 1.0 + 0.5)
    return u


'''
a = randomvector(n+1)
x = bitdecomposevector(a)

c = inversedecomposevec(x)

b = randomvector(n+1)
y = powerof2(b)
print a
print x
print c

print b
print y

print np.dot(a, b)
print np.dot(x, y)


a = randomarray(m, n+1)
x = bitdecomposearray(a)
c = inversedecomposearray(x)

b = randomvector(n+1)
y = powerof2(b)

print a
print x
print c

print b
print y

print np.dot(a[2], b)
print np.dot(x[2], y)

'''


pk, sk = keygen()
for i in range(0, 10):
    print "========"
    C1 = enc(pk, 1)
    C2 = enc(pk, 1)

    print dec(sk, C1)
    print dec(sk, C2)

    C3 = flattenarray(C1 + C2)

    print dec(sk, C3)

    C4 = flattenarray(np.dot(C1, C2))

    print dec(sk, C4)