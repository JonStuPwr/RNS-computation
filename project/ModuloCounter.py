import math
import gmpy2


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


class ModuloCounter:
    def start(self):

        # print(9223372036854775807 % 47)
        # print(gmpy2.f_mod(gmpy2.mpz(9223372036854775807), gmpy2.mpz(47)))

        # x = "1011001111010001010"  # 368266
        # p = "101111"  # 47

        x = dec_int_to_bin_str(9223372036854775807)
        p = dec_int_to_bin_str(47)

        n = len(x)
        r = math.ceil(math.log2(int(p, 2)))
        k = math.ceil(n / r)

        print(f"x: {x}")
        print(f"p: {p}")
        print(f"n: {n}")
        print(f"r: {r}")
        print(f"k: {k}")

        if n < k * r:
            x = con(k, r, n, x)

        subvectors = split_to_subvectors(x, r, k)
        for subvector in subvectors:
            print(subvector)

        s = bin(calculate_sum(k, r, subvectors, int(p, 2)))[2:]
        s_temp = s

        while int(s_temp, 2) > 2 * int(p, 2):

            n_temp = len(s_temp)
            k_temp = math.ceil(n_temp / r)

            if n_temp < k_temp * r:
                s_temp = con(k_temp, r, n_temp, s_temp)
            print(f"s_temp: {s_temp}")

            subvectors_temp = split_to_subvectors(s_temp, r, k_temp)
            for subvector in subvectors_temp:
                print(subvector)

            s_temp = bin(calculate_sum(k_temp, r, subvectors_temp, int(p, 2)))[2:]

        if int(p, 2) <= int(s_temp, 2):
            s = bin(int(s_temp, 2) - int(p, 2))[2:]
        else:
            s = s_temp

        print(int(s, 2))
