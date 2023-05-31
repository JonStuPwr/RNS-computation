from project.AuxiliaryFunctions import *
import math


def calc_mod_function(X_dec, P_dec):
    # tablice bitów, na pierwszym miejscu LSB
    X = dec_to_bin(X_dec)

    # długość ciągu bitów
    n = len(X)

    # liczba bitów w każdym podwektorze
    r = math.ceil(math.log2(P_dec))

    # liczba podwektorów
    k = math.ceil(n / r)

    if n < k * r:
        X = concat(k, r, n, X)

    X_k = split_into_subvectors(X, r, k)

    S = calc_mod_sum(k, r, X_k, P_dec)
    S_temp = S

    count_loops = 0

    while S_temp >= 2 * P_dec:

        S_temp = dec_to_bin(S_temp)

        n_temp = len(S_temp)
        k_temp = math.ceil(n_temp / r)

        if n_temp < k_temp * r:
            S_temp = concat(k_temp, r, n_temp, S_temp)

        S_temp_k = split_into_subvectors(S_temp, r, k_temp)

        S_temp = calc_mod_sum(k_temp, r, S_temp_k, P_dec)

        count_loops += 1

    if P_dec <= S_temp:
        S = S_temp - P_dec
    else:
        S = S_temp

    print(f"S: {S}")
    print(f"loops: {count_loops}\n")

    return count_loops


def interface_mod():
    x = int(input("Podaj X: "))
    p = int(input("Podaj P: "))
    calc_mod_function(x, p)
