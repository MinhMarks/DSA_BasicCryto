def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u, v = extended_gcd(b, a % b)
        return gcd, v, u - (a // b) * v
#or def from cryptohack
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

a, b = map(int, input("Enter two numbers: ").split())
gcd, u, v = extended_gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd}")
print(f"The coefficients u and v are {u} and {v}")
print(f"{a}*{u} + {b}*{v} = {gcd}")

