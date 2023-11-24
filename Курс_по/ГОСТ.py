s_box = [1, 13, 4, 6, 7, 5, 14, 4,
             15, 11, 11, 12, 13, 8, 11, 10,
             13, 4, 10, 7, 10, 1, 4, 9,
             0, 1, 0, 1, 1, 13, 12, 2,
             5, 3, 7, 5, 0, 10, 6, 13,
             7, 15, 2, 15, 8, 3, 13, 8,
             10, 5, 1, 13, 9, 4, 15, 0,
             4, 9, 13, 8, 15, 2, 10, 14,
             9, 0, 3, 4, 14, 14, 2, 6,
             2, 10, 6, 10, 4, 15, 3, 11,
             3, 14, 8, 9, 6, 12, 8, 1,
             14, 7, 5, 14, 12, 7, 1, 12,
             6, 6, 9, 0, 11, 6, 0, 7,
             11, 8, 12, 3, 2, 0, 7, 15,
             8, 2, 15, 11, 5, 9, 5, 5,
             12, 12, 14, 2, 3, 11, 9, 3]

def xor(a, b):
    if len(a) != len(b):
        return None
    str = []
    for k in range(len(a)):
        if a[k] != b[k]:
            str.append('1')
        else:
            str.append('0')
    return ''.join(str)

def in_ASCii(bits, word):

    str = []
    for i in range(bits // 8):
        letter = word[i]
        offset = ord(letter) - ord('А')
        binary = bin(192 + offset)[2:]
        str.append(binary)
    return ''.join(str)

def xor2_32(a, b):
    trans = 0
    string = []
    for i in range(len(a) - 1, -1, -1):
        sum = int(a[i]) + int(b[i]) + trans
        string.append(str(sum % 2))
        trans = sum // 2
    string.reverse()
    return ''.join(string)

def sub_table(string):
    str = []
    for i in range(8):
        num = 8 * int(string[i * 4]) + 4 * int(string[i * 4 + 1]) + 2 * int(string[i * 4 + 2]) + int(string[i * 4 + 3])
        sub_num = s_box[8 * (num) + i]
        binary_sub_num = bin(sub_num)[2:].zfill(4)
        str.append(binary_sub_num)
    return ''.join(str)

def ShiftLeft11(string):
    shift=11
    str = ['.'] * len(string)
    for i in range(len(string)):
        flag = i - shift
        if flag < 0:
            str[len(string) + flag] = string[i]
        else:
            str[flag] = string[i]
    return ''.join(str)


L0 = in_ASCii(32, "ФФФФ")
R0 = in_ASCii(32, "ФФФФ")
X0 = in_ASCii(32, "ФФФФ")
print("L0:", L0)
print("R0:", R0)
print("X0:", X0)
sumX0_R0 = xor2_32(R0, X0)
print("(𝑅0+𝑋0) 𝑚𝑜𝑑 2^32: ", sumX0_R0)
sub_Sbox = sub_table(sumX0_R0)
print("Результат заполнения:",sub_Sbox)
shift = ShiftLeft11(sub_Sbox)
print("Сдвиг на 11 бит влево:",shift)
R1 = xor(shift, L0)
L1=R0
print("L1: ",L1)
print("R1: ", R1)
print("Ответ:", L1 + R1)


