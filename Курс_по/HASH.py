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




# p и q выбрать по варианту для Хэширования
p: int = 41
q: int = 29

N: int = p * q

h0: int = 9


alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

table: dict = make_table(alphabet)


surname: str = "фамилия имя отчество"

sur: str = surname.split(" ")[0]

print("Фамилия:", surname)
print(f"Введённое слово: {sur}")
print(f"Длина слова: {len(sur)}")

print("\n", "===" * 3, " Задание№3 Хэширование ", "===" * 3, "\n")


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


