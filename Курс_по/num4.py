import math

def phi(p: int, q: int) :
    return (p - 1) * (q - 1)

def get_d(phi: int, d) :
    while (d < phi):
        if (math.gcd(d, phi) == 1):
            break
        else:
            d += 1
    return d
def get_e(d: int, phi: int) :
    tmp: list[int] = []
    for k in range(1, d):
        if (phi * k + 1) % d == 0:
            e = int((phi * k + 1) / d)
    return e


print("\n", "===" * 3, " Задание№4(ЭЦП)", "===" * 3, "\n")

#Поставить p и q по своему варианту, и H из 3-го задания
p: int = 47
q: int = 41
N: int = p * q
H: int = 262

phi: int = phi(p,q)

# генерация новых Д и Е
d=5
d: int = get_d(phi,d)

e: int = get_e(d, phi)


S: int = (H ** d) % N

m: int = (S ** e) % N


print("\n", "===" * 3, "Создание подписи", "===" * 3, "\n")
print("Секретный ключ","(", d,",",N,")")
print("Открытый ключ","(", e,",",N,")")
print("Зашифрованное=", S)
print("Расшифрованное =", m)


print()
print(f"Проверка H & m: {H} & {m} = {H == m}")
