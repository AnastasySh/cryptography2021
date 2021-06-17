def getAlfa():  # генерация словарей
    alfa = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
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
    message = message.lower()
    return message


def encrypt(message, alfa, key):
    crypt = ''
    for c in range(len(message)):
        # Номер буквы текста + номер буквы ключа
        crypt += alfa[(alfa.index(message[c]) +
                       alfa.index(key[c % len(key)])) % 32]
    return crypt

#message = input('Введите сообщение:').replace(" " ,"")
#key = input('Введите ключ:')


def decrypt(message, alfa, key):
    decrypt = ''
    for c in range(len(message)):
        decrypt += alfa[(alfa.index(message[c]) -
                         alfa.index(key[c % len(key)])+32) % 32]
    return decrypt


def main(mode, file, message, key):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    alfa = getAlfa()
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
    #name, mode, file, message = argv
    name, mode, key, file, message = 1, 0, 'сегодня', True, '1000char.txt'
    main(mode, file, message, key)
