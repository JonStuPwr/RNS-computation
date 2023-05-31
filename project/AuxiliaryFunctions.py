import random


def generate_random_bit_sequence(length):
    bit_array = []
    for _ in range(length):
        random_bit = random.choice([0, 1])
        bit_array.append(random_bit)
    bit_array[-1] = 1
    return bit_array


# konkatenacja zer
def concat(k, r, n, bit_array):
    num_of_zeros = k * r - n
    return bit_array + [0] * num_of_zeros


# podział liczby binarnej na podwektory
def split_into_subvectors(bit_array, subvector_length, num_of_subvectors):
    subvectors = []
    for i in range(num_of_subvectors):
        start_index = i * subvector_length
        end_index = start_index + subvector_length
        subvector = bit_array[start_index:end_index]
        subvectors.append(subvector)
    return subvectors


# zamiana liczby binarnej na dziesiętną
def bin_to_dec(bit_array):
    decimal_number = 0
    for bit in reversed(bit_array):
        decimal_number = (decimal_number << 1) | bit
    return decimal_number


# zamiana liczby dziesiętnej na ciąg bitów (string)
def dec_to_bin(decimal_num):
    # Konwersja na łańcuch binarny, pomijając prefiks '0b'
    binary_string = bin(decimal_num)[2:]

    # Konwersja łańcucha na tablicę bitów
    bit_array = [int(bit) for bit in binary_string]

    # Odwrócenie tablicy bitów, aby indeks zerowy odpowiadał najmniej znaczącemu bitowi
    bit_array.reverse()

    return bit_array


# Liczy S_temp dla funkcji modulo
def calc_mod_sum(k, r, subvectors, P_dec):
    result = 0
    for i in range(k):
        result += bin_to_dec(subvectors[i]) * (pow(2, r * ((i + 1) - 1)) % P_dec)
    return result


# Liczy S_temp dla mnożenia modulo
def calc_s_temp(k, r, A_k, B_k, P_dec):
    result = 0
    for i in range(k):
        for j in range(k):
            result += (bin_to_dec(A_k[i]) * bin_to_dec(B_k[j]) * pow(2, r * ((i + 1) + (j + 1) - 2))) % P_dec
    return result


# Liczy S_temp_2 dla mnożenia modulo
def calc_s_temp_2(k, r, subvectors, P_dec):
    result = 0
    for i in range(k):
        result += (bin_to_dec(subvectors[i]) * pow(2, r * ((i + 1) - 1))) % P_dec
    return result
