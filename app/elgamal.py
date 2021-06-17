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


def modInverse(e, el):
    e = e % el
    for x in range(1, el):
        if ((e * x) % el == 1):
            return x
    return 1


def checkPrime(a):
    if a < 32:
        print("число должно быть больше мощности алфавита")
        return 1
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
        return 0
    else:
        print("выберете P заново. Число должно быть простым.")
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

    if mode != 0:
        p = 4
        while checkPrime(p) == 1:
            p = input("Введите P \n")
            p = int(p)
        g = 1
        while checkG(g, p) == 1:
            q = input("Введите Q \n")
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

    # отправитель выбирает случайное целое число X,1<x<(p-1)

    y = (g**x) % p
    print("Открытый ключ(Y)={}, Секретный ключ(X)={}".format(y, x))
    print()
    MAINkey = [y, x]
    # переводим сообщение сообщение
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
    print()
    crypto = []
    for m in alpha_code_msg:
        print("буква: " + alphavit2.get(m))
        print("числовое обозначение: "+str(m))
        # генерация случайного целого числа K
        if mode == 0:
            k = 1
            while True:
                k = random.randint(1, p-2)
                if gcd(k, p-1) == 1:
                    print("K =", k)
                    break
        elif mode == 1:
            while checkK == 1:
                k = input("Введите K:")
                k = int(k)
        # отправитель вычисляет число целое число а
        a = (g**k) % p
        # вычисляем b
        b = ((y**k)*m) % p
        shiphr = (a, b)
        crypto.append(shiphr)
        print("шифробозначение: ({},{})".format(a, b))
        print()

    # расшифровка b = m * a(mod P)
    # m = b\a
    word = ''
    mass = []
    for sh in crypto:
        a = sh[0]
        b = sh[1]
        m = (modInverse(a**x, p) * b) % p
        print("m={}".format(m))
        print("буква: {}".format(alphavit2.get(m)))
        mass.append(alphavit2.get(m))
    word = word.join(mass)
    print("слово: {}".format(word))
    
    return crypto, word, MAINkey


def main(message, file, mode):

    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    newstr,decrypto, key = elgamal(message, mode)
    return(newstr,decrypto, key)
    if file:
        f = open('crypt'+name, 'w')
        f.write(str(newstr))


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 0, True, 'variant.txt'
    main(message, file, mode)
