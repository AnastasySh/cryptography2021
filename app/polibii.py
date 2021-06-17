def getAlfa():  # генерация словарей
    alfaNum = {"А": "11", "Б": "12", "В": "13",
               "Г": "14", "Д": "15", "Е": "16",
               "Ж": "21", "З": "22", "И": "23", "Й": "24",
               "К": "25", "Л": "26", "М": "31", "Н": "32",
               "О": "33", "П": "34", "Р": "35", "С": "36",
               "Т": "41", "У": "42", "Ф": "43", "Х": "44",
               "Ц": "45", "Ч": "46", "Ш": "51", "Щ": "52",
               "Ъ": "53", "Ы": "54", "Ь": "55", "Э": "56",
               "Ю": "61", "Я": "62"}
    numAlfa = dictionary = {"11": "А", "12": "Б", "13": "В",
                            "14": "Г", "15": "Д", "16": "Е", "21": "Ж", "22": "З", "23": "И", "24": "Й",
                            "25": "К", "26": "Л", "31": "М", "32": "Н",
                            "33": "О", "34": "П", "35": "Р", "36": "С",
                            "41": "Т", "42": "У", "43": "Ф", "44": "Х",
                            "45": "Ц", "46": "Ч", "51": "Ш", "52": "Щ",
                            "53": "Ъ", "54": "Ы", "55": "Ь", "56": "Э",
                            "Ю": "61", "Я": "62"}
    dictionary = (alfaNum, numAlfa)
    return dictionary


def preprocessing(mod, message):

    if mod == 0:
        message = message.replace('\n', '')
        message = message.replace('-', '')
        message = message.replace('?', '')
        message = message.replace('+', '')
        message = message.replace('=', '')
        message = message.replace(' ', '')
        message = message.replace(',', 'зпт')
        message = message.replace('.', 'тчк')
        message = message.upper()
    else:
        message = [message[i:i+2] for i in range(0, len(message), 2)]
    return message


def crypt(message):
    cryptMessage = []
    dictionary = getAlfa()[0]
    for char in message:
        cryptMessage.append(dictionary.get(char))
    return cryptMessage


def postprocessing(message):
    message = message.lower()
    message = message.replace('зпт', ',')
    message = message.replace('тчк', '.')

    return message


def encrypt(message):
    cryptMessage = []
    dictionary = getAlfa()[1]
    for char in message:
        cryptMessage.append(dictionary.get(char))
    return cryptMessage


def main(mod, file, message):
    if file:
        name = message
        f = open(message)
        message = f.read()
    if mod == 0:
        message = preprocessing(mod, message)
        cryptMessage = crypt(message)
        newstr = ''.join(cryptMessage)
        return(newstr)
    else:
        message = preprocessing(mod, message)
        cryptMessage = encrypt(message)
        newstr = ''.join(cryptMessage)
        newstr = postprocessing(newstr)
        return(newstr)
    #f = open('crypt'+name, 'w')
    #f.write(newstr)


if __name__ == '__main__':
    from sys import argv
    name, mod, file, message = argv
    #name, mod, file, message = 3, 0, True, "variant.txt"
    main(mod, file, message)
