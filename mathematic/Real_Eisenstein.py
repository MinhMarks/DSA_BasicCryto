#better real eisenstein

import math
from sage.all import *
from decimal import *
getcontext().prec = 100

FLAG = ""
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

ct = 1350995397927355657956786955603012410260017344805998076702828160316695004588429433

n = len(PRIMES)
rows, cols = (n+1, n+2)

M = Matrix(ZZ, rows, cols)
M[0,0], M[0,1] = ct, 1
for i in range(len(PRIMES)):
    M[i+1,0] = round((16**64)*sqrt(PRIMES[i]))
    M[i+1,i+2] = 1

fun = M.LLL()

for i in fun[0]:
    if i == 0:
        break
    FLAG += (chr(abs(i)))
print(FLAG)