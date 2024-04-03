def mul_mod(a, b, mod):
    return ((a % mod)*(b % mod)) % mod


def pow_mod1(a, b, mod, binpow):
    #print(f"\na= {a} b= {b} mod= {mod} binpow= {binpow}")
    b2 = b // 2
    k = b % 2
    #print(f"b2= {b2} k= {k}")
    if b == 0: return 1
    if b == 1: return binpow

    next_binpow = mul_mod(binpow ,binpow ,mod)
    #print(f"next_binpow= {next_binpow}")
    next_pow = pow_mod1(a, b2, mod, next_binpow)
    #print(f"next_binpow= {next_binpow} next_pow= {next_pow}")
    if k==1:
        result = mul_mod(binpow, next_pow, mod)
        #print(f"result = mul_mod(binpow, next_pow, mod) = {result}")
    else:
        result = next_pow
        #print(f"result = next_pow = {result}")
    #print(f"result== {result}")
    return result


p = 991
g = 209
for i in range(p):
   if(mul_mod(i, g, p)==1):
       print(i)
       break
