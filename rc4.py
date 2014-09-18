'''
created on : 18-Sep-2014
@author: Sumit Jain [sumitjain3492@gmail.com]
This is python implementation of RC4 stream cipher.

Encrypt: use method encrypt by passing raw data and key
Decrypt: use method decrypt by passing encrypted data and key

the encrypted data will be generated in base64 encoding
the decrypted data will be in string format

'''
import sys

def KSA(key):
    key_length = len(key)

    a= range(256)

    j = 0
    for i in range(256):
        j = (j + a[i] + key[i % key_length]) % 256
        a[i], a[j] = a[j], a[i]    #swapping

    return a


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swapping

        K = S[(S[i] + S[j]) % 256]
        yield K


def key_conversion(key):
    key=[ord(c) for c in key]
    
    #KSA Step
    S=KSA(key)

    #PRGA Step
    keystream=PRGA(S)
    return keystream


def encrypt(data,key):
    keystream=key_conversion(key)
    out=[]
    for char in data:
        out.append("%02X" % (ord(char) ^ keystream.next()))
    
    hex_data=''.join(out)

    return hex_data.decode('hex').encode('base64').strip()

    

def decrypt(data,key):
    data=data.decode('base64')
    out=[]
    keystream=key_conversion(key)

    for char in data:
        out.append("%02X" % (ord(char) ^ keystream.next()))

    hex_data=''.join(out)

    return hex_data.decode('hex').strip()