import sys


def getAlfa():  # генерация словарей
    alfa = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    return alfa


def preprocessing(message):
    message = message.replace('\n', '')
    message = message.replace('-', '')
    message = message.replace('?', '')
    message = message.replace('+', '')
    message = message.replace('=', '')
    message = message.replace(' ', '')
    message = message.replace(',', 'зпт')
    message = message.replace('.', 'тчк')
    message = message.upper()
    return message


def encrypt(message, alfa, key):
    cipher = ''
    for i in range(len(message)):
        x = alfa.find(message[i])
        y = alfa.find(key[i])
        summa = x + y
        modulo = summa % len(alfa)
        cipher += alfa[modulo]
    print(cipher)
    return (cipher)


def decrypt(message, alfa, key):
    decipher = ''
    for i in range(len(message)):
        x = alfa.find(message[i])
        y = alfa.find(key[i])
        razn = x-y
        modulo = razn % len(alfa)
        decipher += alfa[modulo]
    print(decipher)
    return(decipher)


def main(mode, file, message, key_original):
    if file:
        name = message
        f = open(message)
        message = f.read()

    message = preprocessing(message)
    key_original = preprocessing(key_original)

    alfa = getAlfa()

    key = ''
    if len(message) > len(key_original):  # если длина сообщения больше ключа
        # то к ключу прибавляется исходное сообщение в конец
        key = key_original
        for i in range(int(len(message)-len(key_original))):
            key += message[i]
        key += key_original[:len(message) % len(key_original)]
    elif len(message) < len(key_original):
        key = key_original[:len(message)]  # если меньше то ключ обрезается
    elif len(message) == len(key_original):  # если равны, то ключ сохраняется
        key = key_original
    else:
        return('Какая-то ошибка...')
        

    if mode == 0:
        newstr = encrypt(message, alfa, key)
        return(newstr)
    else:
        newstr = decrypt(message, alfa, key)
        return(newstr)
    if file:
        f = open('crypt'+name, 'w')
        f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, message = argv
    name, mode, key, file, message = 1, 0, 'с', True, '1000char.txt'
    main(mode, file, message, key)
