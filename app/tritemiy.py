
def getAlfa():  # генерация словарей
    alfa = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    return alfa


def encrypt(message, alfa):  # функция шифрования
    cryptMessage = ""
    for i in range((len(message))):
        cryptMessage += alfa[(alfa.find(message[i]) + i % 32) % 32]
    return cryptMessage


def decrypt(cryptMmessage, alfa):
    message = ""
    for i in range((len(cryptMmessage))):
        message += alfa[(alfa.find(cryptMmessage[i]) - i % 32) % 32]
    return message


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


def main(mode, file, message):
    if file:
        name = message
        f = open(message)
        message = f.read()
    print(message)
    message = preprocessing(message)
    alfa = getAlfa()
    if mode == 0:
        newstr = encrypt(message, alfa)
        return(newstr)
    else:
        newstr = decrypt(message, alfa)
        return(newstr)
    #print(newstr)
    #f = open('crypt'+name, 'w')
    #f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    #name, mode, file, message = argv
    name, mode, file, message = 1, 0, True, '1000char.txt'
    main(mode, file, message)


if __name__ == '__main__':
    main()

