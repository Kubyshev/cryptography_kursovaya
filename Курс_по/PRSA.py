import math


def generate_keys():
    #Числа по вариантам
    p = 47
    q = 41

    n = p * q
    e = 0
    phi = (p - 1) * (q - 1)
    print(n,phi)
    d = 5
    while (d < phi):
        if (math.gcd(d, phi) == 1):
            break
        else:
            d += 1
    for k in range(1, d):
        if (phi * k + 1) % d == 0:
            e = int((phi * k + 1) / d)
    return ((e, n), (d, n))

def encrypt(public_key,num):
    e,n = public_key
    C=(num**e)%n
    return C
def decrypt(private_key,num):
    d,n=private_key
    C=(num**d)%n
    return C


public_key, private_key = generate_keys()
encrypted_message = encrypt(public_key, 262)

print(public_key)
print("Зашифрованное сообщение:", encrypted_message)
print(private_key)
decrypt_messege=decrypt(private_key,encrypted_message)
print("Расшифрованное сообщение",decrypt_messege)

