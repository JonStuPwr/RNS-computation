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


def count_modulo_multiplication(a_dec, b_dec, p_dec, r):
    a = dec_int_to_bin_str(a_dec)
    b = dec_int_to_bin_str(b_dec)
    p = dec_int_to_bin_str(p_dec)

    n_a = len(a)
    n_b = len(b)
    n = n_a

    if n_a < n_b:
        n = n_b

    print(f"A: {int(a, 2)}, {a}")
    print(f"B: {int(b, 2)}, {b}")
    print(f"P: {int(p, 2)}, {p}")
    print(f"n: {n}")

    k = math.ceil(n / r)

    if n_a < k * r:
        a = con(k, r, n_a, a)

    if n_b < k * r:
        b = con(k, r, n_b, b)

    print(f"A_con: {int(a, 2)}, {a}")
    print(f"B_con: {int(b, 2)}, {b}")

    a_subvectors = split_to_subvectors(a, r, k)
    b_subvectors = split_to_subvectors(b, r, k)

    print(f"podwektory A:")
    for subvector in a_subvectors:
        print(subvector)

    print(f"podwektory B:")
    for subvector in b_subvectors:
        print(subvector)

    # s = bin(calculate_sum(k, r, subvectors, int(p, 2)))[2:]
    # s_temp = s
    #
    # count_loops = 0
    #
    # while int(s_temp, 2) >= 2 * int(p, 2):
    #
    #     n_temp = len(s_temp)
    #     k_temp = math.ceil(n_temp / r)
    #
    #     if n_temp < k_temp * r:
    #         s_temp = con(k_temp, r, n_temp, s_temp)
    #
    #     subvectors_temp = split_to_subvectors(s_temp, r, k_temp)
    #
    #     s_temp = bin(calculate_sum(k_temp, r, subvectors_temp, int(p, 2)))[2:]
    #
    #     count_loops += 1
    #
    # if int(p, 2) <= int(s_temp, 2):
    #     s = bin(int(s_temp, 2) - int(p, 2))[2:]
    # else:
    #     s = s_temp
    #
    # # print(f"S: {int(s, 2)}")
    # # print(f"count_loops: {count_loops}\n")
    # # zwraca wynik modulo i ilość iteracji
    # return count_loops


def interface():
    a = int(input("Podaj A: "))
    b = int(input("Podaj B: "))
    p = int(input("Podaj P: "))
    r = int(input("Ile bitów w podwektorze: "))

    count_modulo_multiplication(a, b, p, r)
