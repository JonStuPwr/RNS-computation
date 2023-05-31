from project.ModuloFunction import *


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
                x_bit = generate_random_bit_sequence(x_len)
                p_bit = generate_random_bit_sequence(p_len)
                loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
            x_bit = generate_random_bit_sequence(x_len)
            p_bit = generate_random_bit_sequence(p_len)
            loops = calc_mod_function(x_bit, p_bit)

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
