def getAlfa():  # генерация словарей
    alfa = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    num = [i for i in range(0, 32)]
    dictionary = {}
    iterNum = iter(num)
    for ch in alfa:
        n = next(iterNum)
        dictionary.update({ch: alfa[len(alfa)-n-1]})
    return dictionary


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


def crypt(message):
    dictionary = getAlfa()
    cryptMessage = []
    decryptMessage = []
    for char in message:
        cryptMessage.append(dictionary.get(char))
    for char in cryptMessage:
        decryptMessage.append(dictionary.get(char))
    cryptMessage = ''.join(cryptMessage)
    decryptMessage = ''.join(cryptMessage)
    return cryptMessage, message

'''def main(message):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    cryptMessage = crypt(message)
    newstr = ''.join(cryptMessage)
    print(newstr)
    f = open('crypt'+name, 'w')
    f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    name, file, message = argv
    #name, file, message = 3, True, "1000char.txt"
    main(message)
'''