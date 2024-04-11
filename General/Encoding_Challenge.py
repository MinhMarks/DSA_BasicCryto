# TRY THIS FOR ALL TYPE OF available DATA 

from pwn import * # pip install pwntools
import json
import base64 
import codecs
from Crypto.Util.number import long_to_bytes
import binascii

def decode(t, given): 
    
    if t == 'base64':
        return base64.b64decode(str(given)).decode('utf-8')
    elif t == 'hex': 
        return bytes.fromhex(given).decode()
    elif t == 'bigint': 
        return long_to_bytes(given)
    elif t == 'rot13':
        return codecs.encode(given, 'rot_13')
    elif t == 'utf-8':
        s = ""
        for c in given:
            s += chr(c)
        return s
