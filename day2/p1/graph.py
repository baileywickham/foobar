def solution(n, b):
    g = []
    g.append(n)
    while True:
        n = next(n, b)
        if n in g:
            return len(g) - g.index(n)
        g.append(n)


def next(n, b):
    k = len(n)
    # x and y are str type
    # They have aleady been padded
    x = padded(decending(n), k)
    y = padded(accending(n), k)

    z = str_base(int(x, b) - int(y, b), b)
    z = padded(z,k)
    return z

def accending(n):
    return ''.join(x for x in sorted(list(n)))


def decending(n):
    return ''.join(x for x in sorted(list(n), reverse=True))

def padded(x, k):
    while len(x) < k:
        x = '0' + x
    return x

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)


