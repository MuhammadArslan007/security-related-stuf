def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

def gen_e(phi):
    e = 2
    while True:
        if gcd(e,phi) == 1:
            break
        e += 1
    return e
def gen_d(e,phi,d=1):
    while True:
        if (e*d) % phi == 1:
            break
        d += 1
    return d


p = 101
q = 113
n = p*q
phi = (p-1)*(q-1)
e = gen_e(phi)
d = gen_d(e,phi)

print(f"""
p: {p},
q: {q},
n: {n},
phi: {phi},
e: {e},
d: {d}
 """)

msg = "make my msg secret"

def encrypt(msg:str,e:int,n:int) -> str:
    encrypted = ''
    for m in msg:
        ucode:int = ord(m)
        enc = chr(ucode**e % n) 
        encrypted += enc
    return encrypted
d_msg = encrypt(msg, e, n)
print(d_msg)

def decrypt(d_msg:str, d:int, n:int)->str:
    decrypted =  ''
    for m in d_msg:
        ucode = ord(m)
        dec = chr(ucode**d % n)
        decrypted += dec
    return decrypted

e_msg = decrypt(d_msg, d, n)
print(e_msg)
