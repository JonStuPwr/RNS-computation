import random
import math


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
    for i in range(1, k + 1):
        for j in range(1, k + 1):

            power = pow(2, r * (i + j - 2)) % P_dec
            file_name = "./truth_tables_Stemp/table_{}_bits_mod_{}_{}_Stemp.txt".format(r, P_dec, power)

            with open(file_name, 'r') as f:
                for line in f:
                    operands = line.split('\t')
                    A = operands[0]
                    B = operands[1]

                    if (bin_to_dec(A_k[i - 1])) == int(A, 2) and (bin_to_dec(B_k[j - 1]) == int(B, 2)):
                        R = operands[2]
                        # print(A + " " + B + " " + R)
                        result += int(R, 2)
    return result


# Liczy S_temp_2 dla mnożenia modulo
def calc_s_temp_2(k, r, subvectors, P_dec):
    result = 0
    for i in range(1, k+1):

        power = pow(2, r * (i - 1)) % P_dec
        file_name = "./truth_tables_Stemp2/table_{}_bits_mod_{}_{}_Stemp2.txt".format(r, P_dec, power)

        with open(file_name, 'r') as f:
            for line in f:
                operands = line.split('\t')
                X = operands[0]

                if bin_to_dec(subvectors[i - 1]) == int(X, 2):
                    R = operands[1]
                    # print(X + " " + R)
                    result += int(R, 2)
    return result


def create_truth_tables_s_temp(k, r, P_dec):
    powers = []

    for i in range(1, k + 1):
        for j in range(1, k + 1):
            power = pow(2, r * (i + j - 2)) % P_dec
            power_exists = powers.count(power)
            if power_exists == 0:
                powers.append(power)

    max_number = 2 ** r
    P_len = math.ceil(math.log2(P_dec))

    for power in powers:
        new_file = "./truth_tables_Stemp/table_{}_bits_mod_{}_{}_Stemp.txt".format(r, P_dec, power)
        with open(new_file, 'w') as f:
            for i in range(max_number):
                for j in range(max_number):
                    a_bin = bin(i)[2:].zfill(r)
                    b_bin = bin(j)[2:].zfill(r)
                    r_bin = bin((i * j * power) % P_dec)[2:].zfill(P_len)
                    f.write(str(a_bin) + '\t' + str(b_bin) + '\t' + str(r_bin) + '\n')
        f.close()


def create_truth_tables_s_temp_2(k, r, P_dec):
    powers = []

    for i in range(1, k + 1):
        power = pow(2, r * (i - 1)) % P_dec
        power_exists = powers.count(power)
        if power_exists == 0:
            powers.append(power)

    max_number = 2 ** r
    P_len = math.ceil(math.log2(P_dec))

    for power in powers:
        new_file = "./truth_tables_Stemp2/table_{}_bits_mod_{}_{}_Stemp2.txt".format(r, P_dec, power)
        with open(new_file, 'w') as f:
            for i in range(max_number):
                x_bin = bin(i)[2:].zfill(r)
                r_bin = bin((i * power) % P_dec)[2:].zfill(P_len)
                f.write(str(x_bin) + '\t' + str(r_bin) + '\n')
        f.close()
