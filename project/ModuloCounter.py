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


def count_modulo(x_dec, p):
    x = dec_int_to_bin_str(x_dec)
    # p = dec_int_to_bin_str(p_dec)

    n = len(x)
    r = math.ceil(math.log2(int(p, 2)))
    k = math.ceil(n / r)

    # print(f"x: {int(x, 2)}")
    # print(f"p: {int(p, 2)}")
    # print(f"n: {n}")
    # print(f"r: {r}")
    # print(f"k: {k}")

    if n < k * r:
        x = con(k, r, n, x)

    subvectors = split_to_subvectors(x, r, k)

    s = bin(calculate_sum(k, r, subvectors, int(p, 2)))[2:]
    s_temp = s

    count_loops = 0

    while int(s_temp, 2) > 2 * int(p, 2):

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

    # print(f"s: {int(s, 2)}")
    # print(f"count_loops: {count_loops}\n")
    # zwraca wynik modulo i ilość iteracji
    return int(s, 2), count_loops


def test():

    num_of_bits = 64
    sum_of_loops = []

    # max_x = 0
    # max_p = 0
    # max_result = 0
    # max_loops = 0

    # pomiary dla p (uśrednione x)
    f = open('result_for_p.txt', 'w')

    index = 0
    for i in range(2, num_of_bits + 1):  # p
        print(i)
        sum_of_loops.append(0)
        for j in range(1, (pow(2, num_of_bits) - 1) + 1):  # x
            result, loops = count_modulo(j, '1' * i)
            sum_of_loops[index] += loops
        f.write(str(i))
        f.write('\t')
        f.write(str(sum_of_loops[index] / (pow(2, num_of_bits))))
        f.write('\n')
        index += 1
    f.close()

    # for p in range(1, (pow(2, num_of_bits) - 1) + 1):
    #     for x in range(2, (pow(2, num_of_bits) - 1) + 1):
    #
    #         result, loops = count_modulo(x, p)
    #         sum_of_loops += loops
    #         f.writelines(lines)
    #
    #         if result > max_loops:
    #             max_x = x
    #             max_p = p
    #             max_result = result
    #             max_loops = loops

    # results.append([x, p, result, loops])

    # for result in results:
    #     if result[3] > max_loops:
    #         max_x = result[0]
    #         max_p = result[1]
    #         max_result = result[2]
    #         max_loops = result[3]

    # print(f"max_x: {max_x}")
    # print(f"max_p: {max_p}")
    # print(f"max_result: {max_result}")
    # print(f"max_loops: {max_loops}")
