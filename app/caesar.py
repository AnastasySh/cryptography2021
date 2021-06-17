def getAlfa():  # генерация словарей
    alfa = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    num = [i for i in range(0, 32)]
    alfaNum = {}
    numAlfa = {}
    iterNum = iter(num)
    for ch in alfa:
        n = next(iterNum)
        alfaNum.update({ch: n})
        numAlfa.update({n: ch})
        dictionary = (alfaNum, numAlfa)
    return dictionary


def convert(message, number=False):  # конвертирование текста в числа и обратно
    charNum = []
    if(number):
        dictionary = getAlfa()[1]
    else:
        message = message.lower()
        dictionary = getAlfa()[0]
    for symbol in message:
        charNum.append(dictionary[symbol])
    return charNum


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
    return(message)


def crypt(shift, message):
    cryptMessage = []
    for char in message:
        cryptMessage.append((char + shift) % 32)
    return cryptMessage


def encrypt(shift, message):
    cryptMessage = []
    for char in message:
        cryptMessage.append((char - shift) % 32)
    return cryptMessage


def main(mod, shift, message):
    if file:
        name = message
        f = open(message)
        message = f.read()
    message = preprocessing(message)
    message = convert(message)
    if mode == 0:
        cryptMessage = crypt(shift, message)
    else:
        cryptMessage = encrypt(shift, message)
    cryptMessage = convert(cryptMessage, True)
    newstr = ''.join(cryptMessage)
    print(newstr)
    f = open('crypt'+name, 'w')
    f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    # name, mode, file, shift, message = argv
    name, mode, file, shift, message = 'цезарь', 1, True, 3, "1000char.txt"
    main(mode, shift, message)
