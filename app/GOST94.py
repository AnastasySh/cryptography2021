import random


def checkPrime(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
        return 0
    else:
        print("выберете число заново. Число должно быть простым.")
    return 1


def checkPrimeQ(a, p):
    k = 0
    if a < 2:
        print("выберите другое число")
        return 1
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
        if (p-1) % a == 0:
            return 0
        else:
            print("Число должно быть простым сомножителем числа Р-1")
            return 1
    else:
        print("выберете число заново. Число должно быть простым.")
    return 1


def checkA(a, q, p):
    if a < 1 or a > p-1:
        print("а больше 1  до р-1")
        return 1
    if a**q % p == 1:
        return 0
    else:
        print("а^q mod p не равно 1")
        return 1


def checkX(x, q):
    if x < 1 or x > q:
        print("x должно быть меньше q")
        return 1
    else:
        return 0


def checkK(x, q):
    if x < 1 or x > q:
        print("k должно быть меньше q")
        return 1
    else:
        return 0


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


def hash_value(n, alpha_code):
    i = 0
    hash = 1
    while i < len(alpha_code):
        hash = (((hash-1) + int(alpha_code[i]))**2) % n
        i += 1
    return hash


def gost94(msg, mode):
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
    array = []
    array2 = []
    flag = False

    if mode != 0:
        p = 4
        while checkPrime(p) == 1:
            p = input("Введите P \n")
            p = int(p)
        q = 1
        while checkPrimeQ(q, p) == 1:
            q = input("Введите Q \n")
            q = int(q)
        a = -1
        while checkA(a, q, p) == 1:
            a = input("Введите A. 1 < Х ≤ (Р-1) \n")
            a = int(a)
        x = -1
        while checkX(x, p) == 1:
            x = input("Введите X. X должно быть меньше чем q \n")
            x = int(x)
        k = -1
        while checkK(k, p) == 1:
            k = input("Введите K. K должно быть меньше чем q \n")
            k = int(k)
    else:
        # создание массива простых чисел
        for s in range(50, 1000):
            for i in range(2, s):
                if s % i == 0:
                    flag = True
                    break
            if flag == False:
                array.append(s)
            flag = False

        # array.append("...")
        print("Простые числа (s):", array, '\n')
        # генерация P и Q
        p = int(random.choice(array))
        print("p = ", p)
        q = 1

        for s in range(3, p-1):
            for i in range(2, s):
                if s % i == 0:
                    flag = True
                    break
            if flag == False:
                array2.append(s)
            flag = False

        while checkPrimeQ(q, p) == 1:
            q = int(random.choice(array2))
            print(q)
            array2.remove(q)
        print("q = ", q)

        # генерация числа а
        a = 1
        while True:
            a = random.randint(1, p-1)
            if a**q % p == 1:
                print("a =", a)
                break

        # генерация числа x
        array2 = []
        flag2 = False
        for s in range(2, q):
            for i in range(2, s):
                if s % i == 0:
                    flag2 = True
                    break
            if flag2 == False:
                array2.append(s)
            flag2 = False

        x = int(random.choice(array2))
        print("x = ", x)
    # вычисление k
        k = -1
        while k == -1 or k == x:
            k = int(random.choice(array2))
        print("k = ", k)
    # вычисление y
    y = a**x % p

    # вычисление r
    r = (a**k % p) % q
    MAINkey = [p, q, a, x]
    # хэшируем сообщение
    # msg = input("Введите сообщение: ")    # .lower()
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    hash_code_msg = hash_value(p, alpha_code_msg)
    print("Хэш сообщения:= {}".format(hash_code_msg))
    if hash_code_msg == hash_code_msg:
        hash_code_msg = 27
    s = (x*r+k*hash_code_msg) % q

    print("Цифровая подпись = ", r % (2**256), ",", s % (2**256))

    #  Проверка цифровой подписи
    v = (hash_code_msg**(q-2)) % q
    z1 = s*v % q
    z2 = ((q-r)*v) % q
    u = (((a**z1)*(y**z2)) % p) % q
    print(r, " = ", u)
    if u == r:
        print("r = u, следовательно:")
        print("Подпись верна")
    else:
        print("Подпись неверна")
    return (((r % (2**256)), s % (2**256)), MAINkey)


def main(message, file, mode):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    newstr, key = gost94(message, mode)
    return (newstr, key)
    if file:
        f = open('crypt'+name, 'w')
        f.write(str(newstr))


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 1, True, 'variant.txt'
    main(message, file, mode)
