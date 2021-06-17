from ec import DSGOST
import random
# инициализация алфавита


alphavit = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5,
            'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10,
            'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15,
            'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20,
            'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
            'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30,
            'ю': 31, 'я': 32}


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


def hash_value(p, alpha_code_msg):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % p
        i += 1
    return hashing_value


def test_gost_sign(msg, mode):
    global sign, d
    print(msg)
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))

    if mode != 0:
        a = input("введите а: ")
        b = input("введите b: ")
        p = input("введите p: ")
        x = input("введите x: ")
        y = input("введите y: ")
        q = input("введите q: ")
    else:
        p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
        a = 7
        b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
        x = 2
        y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
        q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)
    message = hash_value(p, alpha_code_msg)

    d = random.randint(1, q-1)
    sign = gost.sign(message, d)

    public_key_16x = ""
    public_key_point = str(sign[2])
    for i in range(24, len(public_key_point)-1):
        public_key_16x += public_key_point[i]

    public_key = int(public_key_16x, 16)
    print("Открытый ключ:", public_key)
    print("(", sign[0], ",", sign[1], ")")
    return (p, q, a, x, y, b, public_key, (sign[0], sign[1]))


def test_gost_verify(msg,  p, q, a, x, y, b):
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))

    gost = DSGOST(p, a, b, q, x, y)

    message = hash_value(p, alpha_code_msg)

    public_key = sign[2]
    is_signed = gost.verify(message, sign, public_key)

    if is_signed == True:
        print("Подпись прошла проверку!")
    else:
        print("Беда! Что-то не так!")


def gost12(msg, mode):
    p, q, a, x, y, b, public_key, sign = test_gost_sign(msg, mode)
    test_gost_verify(msg, p, q, a, x, y, b)
    return (sign, [p, q, a, x, y, b, public_key])


def main(message, file, mode):

    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    newstr, key = gost12(message, mode)
    return(newstr, key)
    if file:
        f = open('crypt'+name, 'w')
        f.write(str(newstr))


if __name__ == '__main__':
    from sys import argv
    print(''.join(format(ord(i), 'b') for i in "З"))
    # name, mode, file, shift, message = argv
    name, mode, file, message = '1', 0, True, '1000char.txt'
    main(message, file, mode)
