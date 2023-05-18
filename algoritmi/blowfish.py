s_box=[]

def func(block):
    result = s_box[0][block >> 24]
    result = (result + s_box[1][block >> 16 & 0xff]) % 2 ** 32
    result = result ^ s_box[2][block >> 8 & 0xff]
    result = (result + s_box[3][block & 0xff]) % 2 ** 32
    return result


def encryption(message, p):
    left = message >> 32
    right = message & 0xffffffff

    for round in range(0, 16):
        left = p[round] ^ left
        l_func = func(left)
        right = right ^ func(l_func)
        left, right = right, left

    left, right = right, left
    left = left ^ p[17]
    right = right ^ p[16]
    result = (left << 32) ^ right
    return result

print(encryption(45))