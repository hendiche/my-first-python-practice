print(2**3)


def raise_to_pow(base_num, pow_num):
    result = 1

    for index in range(pow_num):
        result *= base_num

    return result


print(raise_to_pow(2, 3))
