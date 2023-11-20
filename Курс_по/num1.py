g28147 = [1, 13, 4, 6, 7, 5, 14, 4, 15, 11, 11, 12, 13, 8, 11, 10, 13, 4, 10, 7, 10, 1, 4, 9, 0, 1, 0, 1, 1, 13, 12, 2, 5, 3, 7, 5, 0, 10, 6, 13, 7, 15, 2, 15, 8, 3, 13, 8, 10, 5, 1, 13, 9, 4, 15, 0, 4, 9, 13, 8, 15, 2, 10, 14, 9, 0, 3, 4, 14, 14, 2, 6, 2, 10, 6, 10, 4, 15, 3, 11, 3, 14, 8, 9, 6, 12, 8, 1, 14, 7, 5, 14, 12, 7, 1, 12, 6, 6, 9, 0, 11, 6, 0, 7, 11, 8, 12, 3, 2, 0, 7, 15, 8, 2, 15, 11, 5, 9, 5, 5, 12, 12, 14, 2, 3, 11, 9, 3]

def xor(a, b):
    if len(a) != len(b):
        return None
    sb = []
    for k in range(len(a)):
        if a[k] != b[k]:
            sb.append('1')
        else:
            sb.append('0')
    return ''.join(sb)

def ph_1(bits, initData):
    if len(initData) * 8 < bits:
        print("Не хвататет данных для формирования ключа")
        return None
    sb = []
    for i in range(bits // 8):
        letter = initData[i]
        if not (letter >= 'А' and letter <= 'Я' or letter == 'Ё' or letter == ' '):
            print("Ожидались заглавные русские буквы")
            return None
        offset = ord(letter) - ord('А')
        b = bin(192 + offset)[2:]
        sb.append(b)
    return ''.join(sb)

def sumMod32(a, b):
    if len(a) != len(b):
        print("Размеры слагаемых должны быть равны")
        return None
    carry = 0
    sb = []
    for k in range(len(a) - 1, -1, -1):
        sum = int(a[k]) + int(b[k]) + carry
        sb.append(str(sum % 2))
        carry = sum // 2
    sb.reverse()
    return ''.join(sb)

def gosttablesub(a):
    sb = []
    for k in range(8):
        z = 8 * int(a[k * 4]) + 4 * int(a[k * 4 + 1]) + 2 * int(a[k * 4 + 2]) + int(a[k * 4 + 3])
        d = g28147[8 * (z) + k]
        b = bin(d)[2:].zfill(4)
        sb.append(b)
    return ''.join(sb)

def cyclicShiftLeft(a, d):
    sb = ['.'] * len(a)
    for k in range(len(a)):
        k2 = k - d
        if k2 < 0:
            sb[len(a) + k2] = a[k]
        else:
            sb[k2] = a[k]
    return ''.join(sb)

def GOST2817():
    L0 = ph_1(32, "КУБЫ")
    R0 = ph_1(32, "ШЕВА")
    X0 = ph_1(32, "СЕРГ")
    print("L0:", L0)
    print("R0:", R0)
    print("X0:", X0)
    N2_1 = sumMod32(R0, X0)
    print("S=: ", N2_1)
    N2_2 = gosttablesub(N2_1)
    print("исходный",N2_2)
    N2_3 = cyclicShiftLeft(N2_2, 11)
    print("сдвиг",N2_3)
    resultN2_4 = xor(N2_3, L0)
    print("R1=: ", resultN2_4)
    print("GOST:", R0 + resultN2_4)

GOST2817()