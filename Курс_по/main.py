import random


def fi(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def formula(M: list[int], h0: int, n: int) -> list[int]:
    h = [h0]
    for mi in M:
        h.append(((h[-1] + mi) ** 2) % n)
    return h


def make_tablica(alphabet: str) -> dict:
    tablica: dict = {}
    for i, char in enumerate(alphabet):
        tablica[char] = i + 1
    return tablica


def get_M(slovo: str) -> list[int]:
    M: list[int] = list()
    for char in slovo:
        M.append(tablica[char])
    return M


def gcd(x: int, y: int):
    if (y == 0):  # it divide every number
        return x  # return x
    else:
        return gcd(y, x % y)


def get_d(fin: int) -> int:
    tmp: list[int] = []
    for i in range(2, fin):
        if gcd(i, fin) == 1:
            tmp.append(i)
    return random.choice(tmp)


def get_e(d: int, fin: int) -> int:
    tmp: list[int] = []
    for i in range(2, fin):
        # print(i,end=' ')
        if ((d * i) - 1) % fin == 0:
            tmp.append(i)
    return random.choice(tmp)


# TODO: Поставить по варианту (для RSA и Хэширования)
p: int = 41
q: int = 29

N: int = p * q

h0: int = 9


alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


fin = fi(p, q)


tablica: dict = make_tablica(alphabet)


fio: str = "кубышев артём сергеевич"

slovo: str = fio.split(" ")[0]

initials = "".join([s[0] for s in fio.split(" ")])


print("ФИО:", fio)
print(f"Введённое слово: {slovo}")
print(f"Длина слова: {len(slovo)}")
print("Инициалы:", initials)

print("\n", "-_-" * 3, " ZADANIE 3 ", "-_-" * 3, "\n")


M: list[int] = get_M(slovo)

h: int = formula(M, h0, N)

H: int = h[-1]

print("P:", p)
print("Q:", q)
print("n =", N)
print("H[0] =", h0)
print("F(n):", fin)
print("M:", M)
print("H от нулевого до последнего:", h)
print(f"H[{len(h)}] =", H)

print("\n", "-_-" * 3, " ZADANIE 2 (RSA)", "-_-" * 3, "\n")


d: int = get_d(fin)


e: int = get_e(d, fin)


M: list[int] = get_M(initials)

C: list[int] = []
for i in range(len(initials)):
    C.append((M[i] ** e) % N)


D: list[int] = []
for c in C:
    # print(c)
    D.append((c ** d) % N)


print("D:", d)
print("E:", e)
print(f"Формула: {d} * {e} = 1 ( mod {fin} )")
print(f"Формула: {d * e} = 1 ( mod {fin} )")
print("Зашифрованное сообщение:", C)
print("Расшифр сообщение:", D)


print("\n", "-_-" * 3, " ZADANIE 4 (ЭЦП)", "-_-" * 3, "\n")

# TODO: Поставить по варианту (Для ЭЦП)
p: int = 47
q: int = 41

N: int = p * q

fin: int = fi(p, q)

# генерация новых Д и Е
d: int = get_d(fin)

e: int = get_e(d, fin)

S: int = (H ** e) % N

m: int = (S ** d) % N


print("P:", p)
print("Q:", q)
print("F(n):", fin)
print("D:", d)
print("E:", e)
print("S =", S)
print("m =", m)


print()
print(f"Проверка H & m: {H} & {m} = {H == m}")