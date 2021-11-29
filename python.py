#Представить Python-скрипт, позволяющий реализовать операцию сложения столбиком двух целых неотрицательных чисел, в виде файла исходного кода (расширение имени файла - py).
try:
    A = int(input('Введите 1 число: '))
    B = int(input('Введите 2 число: '))
except ValueError as message:
    print('Ошибка ввода')
else:
    maxlen = max(len(str(A)), len(str(B)))
    if(A>B):
        print(' ' * (1 + maxlen - len(str(A))), end = '')
        print(A)

        print(' ' * (1 + maxlen - len(str(B))), end = '')
        print(B)

        print('+', end = '')
        print('_' * maxlen)
    else:
        print(' ' * (1 + maxlen - len(str(B))), end='')
        print(B)

        print(' ' * (1 + maxlen - len(str(A))), end = '')
        print(A)

        print('+', end = '')
        print('_' * maxlen)

    x = 0
    pw = 1
    carry = 0
    p = 10

    for i in range(maxlen):
        print(' ' * (maxlen - i), end='')
        while A > 0 or B > 0:
            a0 = A % 10
            b0 = B % 10

            x += pw * ((a0 + b0 + carry) % 10)
            carry = (a0 + b0 + carry) // 10

            pw *= 10
            A //= 10
            B //= 10

        d = x % p
        print(d // (p // 10))
        p *= 10

    x += pw * carry
    print(x)
