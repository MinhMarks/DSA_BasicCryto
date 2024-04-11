from Crypto.Util.number import bytes_to_long, long_to_bytes
import telnetlib
import json
from sage.all import *
    
HOST = "socket.cryptohack.org"
PORT = 13385

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    st = line[line.find('{'):]
    return json.loads(st)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)
    
tn = telnetlib.Telnet(HOST, PORT)

print(readline())

TARGET = 64
TARGET_BITLEN = 600
ps = gen_strong_pseudoprime(generate_basis(TARGET))
n = 1
for p in ps:
    n *= p
assert(miller_rabin(n, TARGET))

stri = {"prime" : int(n), "base" : int(ps[0])}

to_send = json.loads(json.dumps(stri))
json_send(to_send)
print(to_send, readline())
from json import loads, dumps

def generate_basis(n):
    basis = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if basis[i]:
            basis[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if basis[i]]


def miller_rabin(n, b):
    """
    Miller Rabin test testing over all
    prime basis < b
    """
    basis = generate_basis(b)
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for b in basis:
        x = pow(b, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def crt_backtrack(options, mods, erem, emod):
    if not options:
        return (erem, emod)
    for o in options[0]:
        try:
            c = crt([erem, o], [emod, mods[0]])
            return crt_backtrack(options[1:], mods[1:], c, lcm([mods[0], emod]))
        except ValueError: pass

def gen_strong_pseudoprime(A):
    def app_k(k, S, a):
        kinv = 1/Integers(4*a)(k)
        return set((kinv * (s + k - 1)) % (4*a) for s in S)

    def intersect(x):
        s = x[0]
        for y in x[1:]:
            s &= y
        return s
    S_a = {}
    for a in A:
        s = set()
        p = 3
        while p < 50000:
            if legendre_symbol(a, p) == -1:
                s.add(p % (4*a))
            p = next_prime(p)

        S_a[a] = s
    ks = [1, next_prime(max(A)), next_prime(200)]
    cso, ms = [], []
    for a in A:
        cso.append(list(map(int, intersect([app_k(k, S_a[a], a) for k in ks]))))
        ms.append(4*a)
    ems = [ks[1], ks[2]]
    erem = crt(list(map(int, [ks[1] - pow(ks[2], -1, ks[1]), ks[2] - pow(ks[1], -1, ks[2])])), ems)
    emod = lcm(ems)
    p1, mod = crt_backtrack(cso, ms, erem, emod)
    p1 += ((2**(TARGET_BITLEN // 3 + 3) - p1) // mod) * mod
    while True:
        p2 = ks[1] * (p1 - 1) + 1
        p3 = ks[2] * (p1 - 1) + 1
        if is_prime(p1) and is_prime(p2) and is_prime(p3):
            break
        p1 += mod
    return (p1, p2, p3)