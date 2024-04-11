#Unencryptable

import math
import random
import Crypto
from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes

def pc(a,b,c):
    R=IntegerModRing(c)
    x=R(a)
    return x**b

e = 0x10001
c = 0x5233da71cc1dc1c5f21039f51eb51c80657e1af217d563aa25a8104a4e84a42379040ecdfdd5afa191156ccb40b6f188f4ad96c58922428c4c0bc17fd5384456853e139afde40c3f95988879629297f48d0efa6b335716a4c24bfee36f714d34a4e810a9689e93a0af8502528844ae578100b0188a2790518c695c095c9d677b
n = 0x7fe8cafec59886e9318830f33747cafd200588406e7c42741859e15994ab62410438991ab5d9fc94f386219e3c27d6ffc73754f791e7b2c565611f8fe5054dd132b8c4f3eadcf1180cd8f2a3cc756b06996f2d5b67c390adcba9d444697b13d12b2badfc3c7d5459df16a047ca25f4d18570cd6fa727aed46394576cfdb56b41
k = 0x372f0e88f6f7189da7c06ed49e87e0664b988ecbee583586dfd1c6af99bf20345ae7442012c6807b3493d8936f5b48e553f614754deb3da6230fa1e16a8d5953a94c886699fc2bf409556264d5dced76a1780a90fd22f3701fdbcb183ddab4046affdc4dc6379090f79f4cd50673b24d0b08458cdbe509d60a4ad88a7b4e2921

R = Integers(n)
x = R(k)
value = [R(k-1)]
while x != 1:
    value.append(x+1)
    x = x*x
    
p = []
for i in value:
    if math.gcd(i,n) != 1:
        p.append(math.gcd(i,n))

phi_n = (p[0]-1)*(p[1]-1)

R = IntegerModRing(phi_n)
d = R(1)/R(e)

m = pc(c,d,n)
print(long_to_bytes(Integer(m)))