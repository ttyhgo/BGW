from Util import *
import time

def keygen():
    t = randomvector(n)
    sk = [1]
    for i in t:
        sk.append(i * -1)
    sk = np.remainder(sk, q)
    B = randomarray(m, n)
    e = errorvec(m)

    b = np.dot(B, t) % q + e
    A = np.column_stack([b, B])
    return A, sk

def enc(pk, u):
    R = errorarray(N, m)
    C = flattenarray(u * np.identity(N, int) + bitdecomposearray(np.remainder(np.dot(R, pk), q)))
    return C


def dec(sk, C):
    v = powerof2(sk) % q
    c = 0
    #print v
    for i in range(0, len(v)):
        #print v[i]
        if v[i] <= q/2 and v[i] > q/4:
            #print i
            c = i
            break
    #print C[c]
    #print v[9]
    #print v
    #print sk
    x = np.dot(C[c], v) % q
    #print x, v[c]
    u = int(x*1.0/v[c])
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
print np.dot(x, G.T)

print b
print y

print np.dot(a, b)
print np.dot(x, y)
print np.dot(flattenvec(x), y)
print np.dot(inversedecomposevec(x), b)


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
print np.dot(flattenarray(x)[2], y)
'''

start = time.time()
pk, sk = keygen()
print "KeyGen : %.4lf" %(time.time() - start)

for i in range(0, 10):
    print "========"
    start = time.time()
    C1 = enc(pk, 0)
    print "Enc : %.4f" %(time.time() - start)

    start = time.time()
    C2 = enc(pk, 1)
    print "Enc : %.4f" %(time.time() - start)

    start = time.time()
    print dec(sk, C1)
    print "Dec : %.4f" %(time.time() - start)

    start = time.time()
    print dec(sk, C2)
    print "Dec : %.4f" %(time.time() - start)

    start = time.time()
    C3 = flattenarray(C1 + C2)
    print "Add : %.4f" %(time.time() - start)

    start = time.time()
    print dec(sk, C3)
    print "Dec : %.4f" %(time.time() - start)

    start = time.time()
    C4 = flattenarray(np.dot(C1, C2))
    print "Mul : %.4f" %(time.time() - start)

    start = time.time()
    print dec(sk, C4)
    print "Dec : %.4f" %(time.time() - start)

