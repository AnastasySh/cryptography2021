import random


def preprocessing(message):
    message = message.replace('\n', '')
    message = message.replace('-', '')
    message = message.replace('?', '')
    message = message.replace('+', '')
    message = message.replace('=', '')
    message = message.replace(' ', '')
    message = message.replace(',', 'зпт')
    message = message.replace('.', 'тчк')
    message = message.lower()
    return message


def checkPrime(a):
    if a == -1:
        return -1
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
        return 0
    else:
        print("Число не простое. Измените свой выбор")
    return -1


def RSA(msg, mode):
    # если мы генерируем значения
    if mode == 1:
        # Вычисление массива простых чисел
        array = []
        flag = False
        for s in range(50, 1000):
            for i in range(2, s):
                if s % i == 0:
                    flag = True
                    break
            if flag == False:
                array.append(s)
            flag = False
        print("Простые числа (s):", array, '\n')

        # Простые числа
        p = int(random.choice(array))
        q = int(random.choice(array))
        print("p = %d; q = %d" % (p, q))
    # если мы вбиваем сами
    if mode == 0:
        p = -1
        while checkPrime(p) == -1:
            p = input("Введите P \n")
            p = int(p)
        q = -1
        while checkPrime(q) == -1:
            q = input("Введите Q \n")
            q = int(q)

    n = p * q           # Произведение
    Fn = (p-1)*(q-1)    # Функция Эйлера

    print("n = %d; f(n) = %d\n" % (n, Fn))

    # Подбор открытой экспоненты #
    array2 = []
    for meow in range(2, 10000):
        d = int((1 + 2 * Fn) / meow)
        if d * meow == 1 + 2 * Fn:
            array2.append(meow)

    if array2 == []:
        print("Невозможно найти взаимно простое число D!")
        raise SystemExit

    # array2.append("...")
    print("Подходящие для открытой экспоненты числа(D): ", array2)

    # Открытая экспонента
    # Простое нечётное число не имеющее общих делителей с f(n)
    D = int(random.choice(array2))

    print("Открытая экспонента (E) =", D, '\n')

    k = 2

    # Секретная экспонента
    E = int((1 + k * Fn) / D)

    print("Секретная экспонента(D) =", E)

    # Условие на вычисление секретной экспоненты
    if E * D != 1 + k * Fn:
        raise SystemExit

    public_key = [D, n]      # Публичный ключ
    private_key = [E, n]     # Приватный ключ

    print("Публичный ключ: ", public_key)
    print("Приватный ключ: ", private_key, '\n')

    alphavit = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5,
                'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10,
                'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15,
                'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20,
                'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
                'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30,
                'ю': 31, 'я': 32}

    alphavit2 = {1: 'a', 2: 'б',  3: 'в', 4: 'г', 5: 'д',
                 6: 'е', 7: 'ж', 8: 'з', 9: 'и', 10: 'й',
                 11: 'к', 12: 'л', 13: 'м', 14: 'н', 15: 'о',
                 16: 'п', 17: 'р', 18: 'с', 19: 'т', 20: 'у',
                 21: 'ф', 22: 'х', 23: 'ц', 24: 'ч', 25: 'ш',
                 26: 'щ', 27: 'ъ', 28: 'ы', 29: 'ь', 30: 'э',
                 31: 'ю', 32: 'я'}

    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))

    # хэшируем сообщение
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    print()

    crypto = []
    # Шифрование
    for m in alpha_code_msg:
        Cm = (m ** D) % n
        crypto.append(Cm)
    print("Шифр: ", crypto)

    decrypto = []
    # Расшифрование
    for Cm in crypto:
        Dm = (Cm ** E) % n
        decrypto.append(Dm)
    charDecr = []
    for i in decrypto:
        charDecr.append(alphavit2.get(i))
    decrypto = ''.join(charDecr)
    print("Расшифрованное: ", decrypto)
    key = [public_key, private_key]
    return crypto, decrypto, key


def main(message, file, mode):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    newstr, decrypto, key = RSA(message, mode)
    return(newstr, decrypto, key)
    if file:
        f = open('crypt'+name, 'w')
        f.write(str(newstr))


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 0, True, 'variant.txt'
    main(message, file, mode)
