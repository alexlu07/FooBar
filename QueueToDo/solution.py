def calc_xor(start, length):
    a_mod = (start-1) % 4
    if a_mod == 0:
        a = start-1
    elif a_mod == 1:
        a = 1
    elif a_mod == 2:
        a = start
    else:
        a = 0

    b_mod = (start + length - 1) % 4
    if b_mod == 0:
        b = start + length - 1
    elif b_mod == 1:
        b = 1
    elif b_mod == 2:
        b = start + length
    else:
        b = 0

    return a ^ b

def solution(start, length):
    result = 0
    layer = length
    pos = start
    while layer > 0:
        if pos + layer > 2000000001:
            result ^= calc_xor(pos, 2000000001-pos)
            break
        result ^= calc_xor(pos, layer)

        pos += length
        layer -= 1

    return result

print(solution(0, 3))
