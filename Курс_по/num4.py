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

def formula(M: list[int], h0: int, n: int) -> list[int]:
    h = [h0]
    for mi in M:
        h.append(((h[-1] + mi) ** 2) % n)
    return h


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





print("\n", "===" * 3, " Задание№4(ЭЦП)", "===" * 3, "\n")

#Поставить p и q по своему варианту, и H из 3-го задания
p: int = 47
q: int = 41
N: int = p * q
h0: int = 9


alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

table: dict = make_table(alphabet)


surname: str = "кубышев артём сергеевич"

sur: str = surname.split(" ")[0]

print("Фамилия:", surname)
print(f"Введённое слово: {sur}")
print(f"Длина слова: {len(sur)}")

print("\n", "===" * 3, "Хэширование ", "===" * 3, "\n")


M: list[int] = get_M(sur)

h: int = formula(M, h0, N)

H: int = h[-1]

print("P:", p)
print("Q:", q)
print("n =", N)
print("H[0] =", h0)
print("M:", M)
print("H от нулевого до последнего:", h)
print("H",[len(sur)],"=",H)


fin: int = phi(p, q)

# генерация новых Д и Е
d=5
d: int = get_d(fin,d)

e: int = get_e(d, fin)

S: int = (H ** d) % N

m: int = (S ** e) % N


print("\n", "===" * 3, "Создание подписи", "===" * 3, "\n")
print("Секретный ключ","(", d,",",N,")")
print("Открытый ключ","(", e,",",N,")")
print("Зашифрованное=", S)
print("Расшифрованное =", m)


print()
print(f"Проверка H & m: {H} & {m} = {H == m}")