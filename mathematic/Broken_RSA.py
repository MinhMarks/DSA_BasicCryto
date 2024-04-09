n 
e 
ct 

from number import * 

R.<x> = Zmod(n)[] 
f = x^2 -c 
r8 = [i[0] for i in f.roots() ] 
r4,r2,r = [], [], [] 

for rr8 in r8: 
    f = x^2 - rr8 
    r4 += [i[0] for i in f.roots()]
    
for rr4 in r4: 
    f = x^2 - rr4 
    r2 += [i[0] for i in f.roots()]
    
for rr2 in r2: 
    f = x^2 - rr2 
    r += [i[0] for i in f.roots()]
    
for m in r: 
    print(l2b(m))
    
    