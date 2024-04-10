#!/usr/bin/env python3
import base64 #base64.b64encode() to convert bytes to base64
import sys
from Crypto.Util.number import * #long_to_bytes and bytes_to_long
import pwn 
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

#ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
#hexx="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#rsa= 11515195063862318899931685488813747395775516287289682636499965282714637259206269
string = 'label'
xor_int = 13

value = ''.join(chr(ord(s) ^ xor_int) for s in string)
print (xor('label',13))
print("flag: crypto{%s}" % value)
#print(long_to_bytes(rsa)) 
#print(base64.b64encode(bytes.fromhex(hexx)))
#print("".join(chr(o ^ 0x32) for o in ords))

#for i in range(0, len(ords)) :
 #   print (chr(ords[i]),end='')
