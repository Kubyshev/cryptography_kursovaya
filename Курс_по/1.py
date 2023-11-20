import math
def NOD(a: int, b: int):
    if a > b:  # define the if condition
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd

def phi(p: int, q: int) :
    return (p - 1) * (q - 1)

def make_table(alphabet: str) -> dict:
    table: dict = {}
    for i, char in enumerate(alphabet):
        table[char] = i + 1
    return table


def get_M(word: str) -> list[int]:
    M: list[int] = list()
    for char in word:
        M.append(table[char])
    return M

def get_d(phi: int, d) :
    while (d < phi):
        if (NOD(d, phi) == 1):
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


# p и q поставить по заданию №2
p = 41
q = 29

N= p * q

alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


phi = phi(p, q)


table: dict = make_table(alphabet)


fio: str = "кубышев артём сергеевич"

slovo: str = fio.split(" ")[0]

initials = "".join([s[0] for s in fio.split(" ")])
print("Инициалы:", initials)


print("\n", "===" * 3, " Задние№2 RSA", "===" * 3, "\n")

d=2
d: int = get_d(phi,d)


e: int = get_e(d, phi)


M: list[int] = get_M(initials)

C: list[int] = []
for i in range(len(initials)):
    C.append((M[i] ** e) % N)


D: list[int] = []
for c in C:
    D.append((c ** d) % N)


print("Секретный ключ:","(", d,",",N,")")
print("Открытый ключ:", "(",e,",",N,")")
print("Зашифрованное сообщение:", C)
print("Расшифр сообщение:", D)


