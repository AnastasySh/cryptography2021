from math import gcd
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

# проверка на простое число


def hash_value(p, alpha_code_msg):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % p
        i += 1
    return hashing_value


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

# расширенный алгоритм Евклида или (e**-1) mod fe


def modInverse(e, el):
    e = e % el
    for x in range(1, el):
        if ((e * x) % el == 1):
            return x
    return 1
# выбор простого целого P, выбор целого числа G,G<P


def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = random.randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True


def checkPrime(a):

    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
        return 0
    else:
        print("выберете P")
    return 1


def gen_prime(n):
    found_prime = False
    while not found_prime:
        p = random.randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p


def checkG(g, p):
    if g >= 2 and g <= (p - 1):
        return 0
    else:
        return 1


def checkX(x, p):
    if x >= 2 and x <= (p - 2):
        return 0
    else:
        return 1


def checkK(k, p):
    if 1 > k or k > (p-1):
        return 1
    if gcd(k, p-1) == 1:
        print("K =", k)
        return 0
    else:
        return 1


def elgamal(msg, mode):
    alphavit = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
                'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
                'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
                'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
                'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
                'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
                'ю': 30, 'я': 31, ' ': 32, ",": 33, ".": 34,
                'А': 35, 'Б': 36, 'В': 37, "Г": 38, "Д": 39,
                'Е': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44,
                'К': 45, 'Л': 46, 'М': 47, 'Н': 48, 'О': 49,
                'П': 50, 'Р': 51, 'С': 52, 'Т': 53, 'У': 54,
                'Ф': 55, 'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59,
                'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63, 'Э': 64,
                'Ю': 65, 'Я': 66, '!': 67, "?": 68, ";": 69}
    if mode != 0:
        p = 4
        while checkPrime(p) == 1:
            p = input("Введите P, Р должно быть простым \n")
            p = int(p)
        g = 1
        while checkG(g, p) == 1:
            g = input("Введите G. G должно быть меньше P \n")
            g = int(g)
        x = 1
        while checkX(x, p) == 1:
            x = input("Введите Х. 1 < Х ≤ (Р-1) \n")
            x = int(x)
        k = -1
        while checkK(k, p) == 1:
            k = input("Введите K \n")
            k = int(k)
    else:
        p = gen_prime(10)
        print("P =", p)
        print()
        g = random.randint(2, p-1)
        print("G =", g)
        print()
        x = random.randint(2, p - 2)
        x = int(x)
        k = 1
        while True:
            k = random.randint(1, p-2)
            if gcd(k, p-1) == 1:
                print("K =", k)
                break

    # отправитель выбирает случайное целое число X,1<x<(p-1)

    y = (g**x) % p
    print("Открытый ключ(Y)={}, Секретный ключ(X)={}".format(y, x))
    print()
    MAINkey = [y, x]
    # хэшируем сообщение
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    print()

    hash_code_msg = hash_value(p, alpha_code_msg)
    print("Хэш сообщения:= {}".format(hash_code_msg))
    print()
    # генерация случайное целое число K

    # отправитель вычисляет число целое число а
    a = (g**k) % p
    # вычисляем b
    b = modInverse(k, p-1) * ((hash_code_msg - (x * a)) % (p-1))
    #b = modInverse((int(hash_code_msg) - int(x)*int(a)),p-1)
    #b = (X*a+m) \k
    print("Значение подписи:S={},{}".format(a, b))
    print()

    # провоерка подписи (передвём m, a,b)
    check_hash_value = hash_value(p, alpha_code_msg)
    a_1 = ((y**a) * (a**b)) % p
    print("A1={}".format(a_1))
    print()
    a_2 = (g**check_hash_value) % p
    print("A2={}".format(a_2))
    print()
    if a_1 == a_2:
        print("Подпись верна")
    else:
        print("Подпись неверна")
        return 0
    return ("({},{})".format(a, b), MAINkey)


def main(message, file, mode):

    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    newstr, key = elgamal(message, mode)
    return(newstr, key)
    if file:
        f = open('crypt'+name, 'w')
        f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 1, True, '1000char.txt'
    main(message, file, mode)
