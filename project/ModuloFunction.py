import math
import random


def generate_random_bit_sequence(length):
    bits = []
    for _ in range(length):
        random_bit = random.choice([0, 1])
        bits.append(random_bit)

    bits[0] = 1
    bit_string = "".join(str(bit) for bit in bits)
    return bit_string


# dokleja zera z przodu ciągu (string)
def con(k, r, n, x):
    num_of_zeros = k * r - n
    return '0' * num_of_zeros + x


# dzieli wektor na podwektory, zwraca listę podwektorów (stringi)
def split_to_subvectors(binary_str, subvector_length, num_of_subvectors):
    subvectors = []
    for i in range(num_of_subvectors):
        start_index = i * subvector_length
        end_index = start_index + subvector_length
        subvector = binary_str[start_index:end_index]
        subvectors.insert(0, subvector)
    return subvectors


# liczy sumę "s", zwraca wynik w postaci decymalnej (int)
def calculate_sum(num_of_subvectors, subvector_length, subvectors, p):
    result = 0
    for i in range(num_of_subvectors):
        result += int(subvectors[i], 2) * pow(2, subvector_length * ((i + 1) - 1), p)
    return result


# zamiana liczby dziesiętnej na ciąg bitów (string)
def dec_int_to_bin_str(decimal):
    binary = ''
    if decimal == 0:
        binary = '0'
    else:
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
    return binary


def count_modulo(x, p):
    # x = dec_int_to_bin_str(x_dec)
    # p = dec_int_to_bin_str(p_dec)

    n = len(x)
    r = math.ceil(math.log2(int(p, 2)))
    k = math.ceil(n / r)

    if n < k * r:
        x = con(k, r, n, x)

    subvectors = split_to_subvectors(x, r, k)

    s = bin(calculate_sum(k, r, subvectors, int(p, 2)))[2:]
    s_temp = s

    count_loops = 0

    while int(s_temp, 2) >= 2 * int(p, 2):

        n_temp = len(s_temp)
        k_temp = math.ceil(n_temp / r)

        if n_temp < k_temp * r:
            s_temp = con(k_temp, r, n_temp, s_temp)

        subvectors_temp = split_to_subvectors(s_temp, r, k_temp)

        s_temp = bin(calculate_sum(k_temp, r, subvectors_temp, int(p, 2)))[2:]

        count_loops += 1

    if int(p, 2) <= int(s_temp, 2):
        s = bin(int(s_temp, 2) - int(p, 2))[2:]
    else:
        s = s_temp

    # print(f"S: {int(s, 2)}")
    # print(f"count_loops: {count_loops}\n")
    # zwraca wynik modulo i ilość iteracji
    return count_loops


def interface():
    x = int(input("Podaj X: "))
    p = int(input("Podaj P: "))

    # count_modulo(x, p)


def test():

    f = open('x_range_4_to_128_bit.txt', 'w')
    for x_len in range(4, 128 + 1, 1):
        print(f"x: {x_len}")
        max_loops = 0
        max_x = 0
        max_p = 0
        for p_len in range(2, x_len + 1, 1):
            print(p_len)
            for j in range(0, 100001, 1):
                x_bit_str = generate_random_bit_sequence(x_len)
                p_bit_str = generate_random_bit_sequence(p_len)
                loops = count_modulo(x_bit_str, p_bit_str)

                if loops > max_loops:
                    max_loops = loops
                    max_x = x_len
                    max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    # ------------------------------------- #

    print("x: 4 bit")
    f = open('x_4_bit.txt', 'w')
    x_len = 4
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 8 bit")
    f = open('x_8_bit.txt', 'w')
    x_len = 8
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 16 bit")
    f = open('x_16_bit.txt', 'w')
    x_len = 16
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 32 bit")
    f = open('x_32_bit.txt', 'w')
    x_len = 32
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 64 bit")
    f = open('x_64_bit.txt', 'w')
    x_len = 64
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 128 bit")
    f = open('x_128_bit.txt', 'w')
    x_len = 128
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 256 bit")
    f = open('x_256_bit.txt', 'w')
    x_len = 256
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()

    print("x: 512 bit")
    f = open('x_512_bit.txt', 'w')
    x_len = 512
    for p_len in range(2, x_len + 1, 1):
        print(p_len)
        max_loops = 0
        max_x = 0
        max_p = 0
        for j in range(0, 100001, 1):
            x_bit_str = generate_random_bit_sequence(x_len)
            p_bit_str = generate_random_bit_sequence(p_len)
            loops = count_modulo(x_bit_str, p_bit_str)

            if loops > max_loops:
                max_loops = loops
                max_x = x_len
                max_p = p_len

        f.write(str(max_x))
        f.write('\t')
        f.write(str(max_p))
        f.write('\t')
        f.write(str(max_loops))
        f.write('\n')

    f.close()
