def ec_addition(r1, s1, r2, s2, n):
    m = ((s2 - s1) * pow(r2 - r1, -1, n)) % n
    r_new = (m ** 2 - r1 - r2) % n
    s_new = (m * (r_new - r1) + s1) % n
    s_new = -s_new % n
    return r_new, s_new
def ec_multiplication(a, r, s, b, n):
    r_new, s_new, r_old, s_old = 0, 0, r, s
    bits = bin(b)[3:]
    for bit in bits:
        m = (((3 * (r_old ** 2)) + a) * (pow(2 * s_old, -1, n))) % n
        r_new = (m ** 2 - 2 * r_old) % n
        s_new = -(m * (r_new - r_old) + s_old) % n

        if bit == '1':
            r_new, s_new = ec_addition(r_new, s_new, r, s, n)

        r_old = r_new
        s_old = s_new

    return r_new, s_new
