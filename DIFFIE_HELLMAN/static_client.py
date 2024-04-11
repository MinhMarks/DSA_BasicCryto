from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
import telnetlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sage.all import *


def pohlig_hellman(base,a,p,phi_p,f):
#solves base^x = a mod p
    R = Integers(p)
    g = R(base)
    l = len(f)
    
    ord = phi_p
    l=[0]*len(f)
    for i,(pi,ri) in enumerate(f):
        for j in range(ri):
            c=bsgs(base**(ord//pi),(a//base**l[i])**(ord//pi**(j+1)),(0,pi))
            l[i] += c*(pi**j)
    return crt(l,[pi**ri for pi,ri in f])

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

HOST = "socket.cryptohack.org"
PORT = 13378

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    st = line[line.find('{'):]
    return json.loads(st)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

lim = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633918
lim2 = 782447372963237017080911425690626808320121477344046500785903911140548592900614218375169986555497769722994612768766237489225391319847998034333635622999777018085492552042629201517236242969387773417387518064509930154467125225099893166734205067493594146299578427161129003066430095422159690004313302195831114109968070664752615603031826096360561083674123245084443411780282892018035180938429828776626215527562796692413033621528951604797200401283355182471258495210998412729835889355808886300

weak_primes = []
max_p = 1
p = 1
while len(weak_primes)<3:
    mul1 = 2
    temp_p = p
    while len(weak_primes)<3 and mul1 < lim2:
        mul1 *= temp_p
        temp_p = next_prime(temp_p)
        if is_prime(mul1+1):
            if mul1+1 > lim:
                weak_primes.append(mul1+1)
    max_p = max(max_p,temp_p)
    p += 1

mul1 = 1
phi_n = 1
for i in weak_primes:
    mul1*=i
    phi_n*=(i-1)
    
temp = phi_n
p = 2
fac =[]
while temp>1:
    count = 0 
    while temp%p == 0:
        temp /= p
        count += 1
    if count != 0:
        fac.append([p,count])
    p = next_prime(p)
    
R = Integers(mul1)
g = R(2)
f = [[i,j] for i,j in fac] 
temp = phi_n
for i in range(len(f)):
    while f[i][1]>0 and g**temp == 1:
        f[i][1] -= 1
        temp = int(temp//f[i][0])

    if g**temp != 1:
        f[i][1] += 1
        temp = int(temp*f[i][0])
    
dlogs = []
count = 0
for i in weak_primes:
    tn = telnetlib.Telnet(HOST, PORT)    
    alice = json_recv()
    bob = json_recv()
    flag = json_recv()
    
    stri = '''{"p": "0x1", "g": "0x2", "A": "0x2232"}'''
    pre_alice = json.loads(stri)
    pre_alice['p'] = hex(i)
    
    json_send(pre_alice)
    
    pre_bob = json_recv()
    pre_flag = json_recv()
    
    dlogs.append((int(pre_bob["B"],0)))
    print(count)
    count += 1

while len(dlogs) != len(weak_primes):
    weak_primes.pop()
x = crt(dlogs, weak_primes)

R = Integers(mul1) 
g = R(2)

n = (pohlig_hellman(R(2),R(x),mul1,temp,f))

R = GF(alice["p"])
g = R(alice["g"])
A = R(alice["A"])
B = R(bob["B"])
if g**n == B:
    print("correct")
    key = A**n
    print(decrypt_flag(key, flag['iv'], flag['encrypted']))
else:
    print(n)