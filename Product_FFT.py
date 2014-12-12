#!/usr/bin/python

import cmath
import math
import re

#fft function
#it takes the list for fft and the direction whether forward or invese fft
def fft(x,dir):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2],dir)
    odd =  fft(x[1::2],dir)
    return [even[k] + cmath.exp(-2j*dir*cmath.pi*k/N)*odd[k] for k in xrange(N/2)] + \
           [even[k] - cmath.exp(-2j*dir*cmath.pi*k/N)*odd[k] for k in xrange(N/2)]

#taking first number as input in the form of a string
str1 = raw_input('Input 1 : ')
data1 = map(int, re.findall(r'\d+', str1))

data1.reverse()

#taking second number as input in the form of a string
str2 = raw_input('Input 2 : ')
data2 = map(int, re.findall(r'\d+', str2))

data2.reverse()

n1 = len(data1)
n2 = len(data2)

if n1 > n2:
	n = n1
else:
	n = n2

#taking power of 2 for fft
p = math.log(n,2)
p = math.ceil(p)
p = int(math.pow(2,p+1))

for i in range(0, p - n1):
	data1.append(0)

for i in range(0, p - n2):
	data2.append(0)

#taking fft of both lists
f1 = fft(data1,1)
f2 = fft(data2,1)

C = []

#taking pointwise multiplication
for i in range(0, p):
	C.append(f1[i]*f2[i])

#taking inverse fft
c = fft(C,-1)

ans = []

q = p - 1;

#skipping initial zeroes for printing
while int(c[q].real)==0:
	q = q-1

q = q+1

for i in range(0,q):
	ans.append(int(math.ceil(c[q - 1 - i].real)/(p)))

print "Output :"," ".join(repr(i) for i in ans),"\n"