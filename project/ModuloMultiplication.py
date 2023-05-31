from project.AuxiliaryFunctions import *
import math


def calc_mod_multiplication(A_dec, B_dec, P_dec, r):
    A = dec_to_bin(A_dec)
    B = dec_to_bin(B_dec)

    n_A = len(A)
    n_B = len(B)

    if n_A < n_B:
        n = n_B
    else:
        n = n_A

    k = math.ceil(n / r)

    if n_A < k * r:
        A = concat(k, r, n_A, A)

    if n_B < k * r:
        B = concat(k, r, n_B, B)

    A_k = split_into_subvectors(A, r, k)
    B_k = split_into_subvectors(B, r, k)

    S = calc_s_temp(k, r, A_k, B_k, P_dec)
    S_temp = S

    count_loops = 0

    while S_temp >= 2 * P_dec:

        S_temp = dec_to_bin(S_temp)

        n_temp = len(S_temp)
        k_temp = math.ceil(n_temp / r)

        if n_temp < k_temp * r:
            S_temp = concat(k_temp, r, n_temp, S_temp)

        S_temp_k = split_into_subvectors(S_temp, r, k_temp)

        S_temp = calc_s_temp_2(k_temp, r, S_temp_k, P_dec)

        count_loops += 1

    if P_dec <= S_temp:
        S = S_temp - P_dec
    else:
        S = S_temp

    print(f"S: {S}")
    print(f"loops: {count_loops}\n")


def interface_mul():
    a = int(input("Podaj A: "))
    b = int(input("Podaj B: "))
    p = int(input("Podaj P: "))
    r = int(input("Ile bitów w podwektorze: "))
    calc_mod_multiplication(a, b, p, r)
