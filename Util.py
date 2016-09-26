import numpy as np
from Crypto.Util import number
import math

q = 32
l = int(math.log(q, 2)) + 1
n = 5
m = int(n * math.log(q, 2))
N = (n+1) * l


def bitdecomposition(x):
    bits = []
    i = 1
    while i <= q:
        if i & x:
            bits.append(1)
        else:
            bits.append(0)
        i <<= 1
    return bits

def bitdecomposevector(x):
    bitdecomp = []
    for i in x:
        bitarray = bitdecomposition(i)
        for j in bitarray:
            bitdecomp.append(j)

    return bitdecomp

def bitdecomposearray(a):
    bitdecomp = []
    for raw in a:
        bitarray = bitdecomposevector(raw)
        bitdecomp.append(bitarray)
    return np.array(bitdecomp)

def inversedecomposevec(x):
    inversedecomp = []
    bit = q.bit_length() - 1
    temp = 0
    #print x.__len__(), l
    for i in range(0, x.__len__()):
        temp += x[i] * 2**(i % q.bit_length())
        if i % q.bit_length() is bit:
            inversedecomp.append(temp)
            temp = 0
    return np.array(inversedecomp)

def inversedecomposearray(a):
    inversedecomp = []
    for i in a:
        inverse = inversedecomposevec(i)
        inversedecomp.append(inverse)
    return np.array(inversedecomp)

def flattenvec(x):
    return bitdecomposevector(inversedecomposevec(x))

def flattenarray(a):
    return bitdecomposearray((inversedecomposearray(a)))

def randomvector(length):
    vec = []
    for i in range(0, length):
        vec.append(number.getRandomRange(0, q))
    return np.array(vec)

def randomarray(raw, col):
    array = []

    for i in range(0, raw):
        array.append(randomvector(col))
    return np.array(array)

def powerof2(x):
    result = []
    for i in range(0, len(x)):
        for j in range(0, l):
            result.append(x[i] * 2**j)
    return np.array(result)

def errorvec(length):
    e = []
    for i in range(0, length):
        e.append(number.getRandomInteger(1))
    return np.array(e)

def errorarray(raw, col):
    array = []

    for i in range(0, raw):
        array.append(errorvec(col))
    return np.array(array)
