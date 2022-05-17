"""
Steps:
    Choose two large prime numbers (p and q)
    Calculate n = p*q and z = (p-1)(q-1)
    Choose a number e where 1 < e < z, and e is co-prime with z.
    Calculate d such that [ed = 1 mod z]
    You can bundle private key pair as (n,d)
    You can bundle public key pair as (n,e)
"""

p = 5
q = 3
n = 5*3 # 15
z = (5-1)(3-1) # 8
e = 5 # co-prime with z. Public key.
d = 5 # wd = 1 mod z. Private key.

