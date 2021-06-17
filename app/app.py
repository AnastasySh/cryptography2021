from flask import Flask, request, render_template
app = Flask(__name__)
#application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atbash', methods=['POST', 'GET'])
def atbash():
    import atbash as ATBASH
    if (request.method=='GET'):
        return render_template('zeroarg.html', title='Атбаш')
    if (request.method=='POST'):
        message = request.form.get('message')
        message = ATBASH.preprocessing(message)
        crypto, decrypto = ATBASH.crypt(message)
        return render_template('zeroarg.html', title='Атбаш', crypto=crypto, decrypto=decrypto)
    
@app.route('/caesar', methods=['POST', 'GET'])
def caesar():
    import caesar as CAESAR
    if (request.method=='GET'):
        return render_template('zeroarg.html', title='Шифр Цезаря', atr={'name':"смещение", 'id':"shift"})
    if (request.method=='POST'):
        message = request.form.get('message')
        shift = int(request.form.get('shift'))
        message = CAESAR.preprocessing(message)
        message = CAESAR.convert(message)
        crypto = CAESAR.crypt(shift, message)
        decrypto = CAESAR.encrypt(shift, crypto)
        crypto = CAESAR.convert(crypto, True)
        decrypto = CAESAR.convert(decrypto, True)
        decrypto = ''.join(decrypto)
        crypto = ''.join(crypto)
        return render_template('zeroarg.html', title='Шифр Цезаря', atr={'name':"смещение", 'id':"shift"}, crypto=crypto, decrypto=decrypto)

@app.route('/polibii', methods=['POST', 'GET'])
def polibii():
    import polibii as POLIBII
    if (request.method=='GET'):
        return render_template('zeroarg.html', title='Полибий')
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto = POLIBII.main(0,False, message)
        decrypto = POLIBII.main(1,False, crypto)
        return render_template('zeroarg.html', title='Полибий', crypto=crypto, decrypto=decrypto)

@app.route('/tritemii', methods=['POST', 'GET'])
def tritemii():
    import tritemiy as CRYPTO
    if (request.method=='GET'):
        return render_template('zeroarg.html', title='Шифр Тритемия')
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto = CRYPTO.main(0,False, message)
        decrypto = CRYPTO.main(1,False, crypto)
        return render_template('zeroarg.html', title='Шифр Тритемия', crypto=crypto, decrypto=decrypto)


@app.route('/belazo', methods=['POST', 'GET'])
def belazo():
    import belazo as CRYPTO
    name='Шифр Белазо'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, atr={'name':"ключ", 'id':"key"})
    if (request.method=='POST'):
        message = request.form.get('message')
        key = request.form.get('key')
        crypto = CRYPTO.main(0,False, message,key)
        decrypto = CRYPTO.main(1,False, crypto,key)
        return render_template('zeroarg.html', title=name,atr={'name':"ключ", 'id':"key"}, crypto=crypto, decrypto=decrypto)

@app.route('/viziner', methods=['POST', 'GET'])
def viziner():
    import vijenere as CRYPTO
    name='Шифр Виженера'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, atr={'name':"ключ", 'id':"key"})
    if (request.method=='POST'):
        message = request.form.get('message')
        key = request.form.get('key')
        crypto = CRYPTO.main(0,False, message,key)
        decrypto = CRYPTO.main(1, False, crypto,key)
        return render_template('zeroarg.html', title=name,atr={'name':"ключ", 'id':"key"}, crypto=crypto, decrypto=CRYPTO.preprocessing(message).upper())


@app.route('/matrix', methods=['POST', 'GET'])
def matrix():
    import matrichniy as CRYPTO
    name='Матричный шифр'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, atr={'name':"ключ-матрица в формате '1 4 8 3 7 2 6 9 5'", 'id':"key"})
    if (request.method=='POST'):
        message = request.form.get('message')
        key = request.form.get('key')
        crypto = CRYPTO.main(0, False, message, key)
        crypto = crypto.replace(']','] ')
        print('%%%'+crypto+'%%%')
        crypto = crypto[:-1]
        decrypto = CRYPTO.main(1, False, crypto, key)
        decrypto = decrypto.replace('[', '')
        decrypto = decrypto.replace(']', '')
        decrypto = decrypto.replace(',', '')
        decrypto = decrypto.replace("'", "")
        decrypto = decrypto.replace(" ", "")
        return render_template('zeroarg.html', title=name,atr={'name':"ключ-матрица в формате '1 4 8 3 7 2 6 9 5'", 'id':"key"}, crypto=crypto, decrypto=decrypto)


@app.route('/playfer', methods=['POST', 'GET'])
def playfer():
    import playfer as CRYPTO
    name='Шифр Плейфера'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, atr={'name':"ключ", 'id':"key"})
    if (request.method=='POST'):
        message = request.form.get('message')
        key = request.form.get('key')
        crypto = CRYPTO.main(0,False, message,key)
        decrypto = CRYPTO.main(1, False, crypto,key)
        return render_template('zeroarg.html', title=name,atr={'name':"ключ", 'id':"key"}, crypto=crypto, decrypto=decrypto)


@app.route('/vertical', methods=['POST', 'GET'])
def vertical():
    import vertical_change as CRYPTO
    name='Шифр вертикальной перестановки'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, atr={'name':"ключ", 'id':"key"})
    if (request.method=='POST'):
        message = request.form.get('message')
        key = request.form.get('key')
        crypto = CRYPTO.main(key, message, 0, False)
        decrypto = CRYPTO.main(key, message, 1, False)
        return render_template('zeroarg.html', title=name,atr={'name':"ключ", 'id':"key"}, crypto=crypto, decrypto=CRYPTO.preprocessing(message))


@app.route('/cardano', methods=['POST', 'GET'])
def cardano():
    import reshetka_kardano_final as CRYPTO
    name='Решетка Кардано'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        key, crypto = CRYPTO.main(message, 0, False)
        key, decrypto = CRYPTO.main(message, 1, False, key=key)
        return render_template('zeroarg.html', title=name, crypto=crypto, decrypto=decrypto)

@app.route('/shennon', methods=['POST', 'GET'])
def shennon():
    import shennon as CRYPTO
    name='Шифр Шеннона'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto, decrypto, key = CRYPTO.main(message, 0, False)
        return render_template('zeroarg.html', title=name, crypto=crypto, decrypto=decrypto, key=key)


@app.route('/gost89', methods=['POST', 'GET'])
def gost89():
    import gammir as CRYPTO
    name='Гаммирование ГОСТ 28147-89'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        key, crypto = CRYPTO.main(message, False)
        return render_template('zeroarg.html', title=name,   crypto=crypto,   key=key,    decrypto=message)

@app.route('/A51', methods=['POST', 'GET'])
def A51():
    import A5_first as CRYPTO
    name='A5/1'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto, decrypto, key = CRYPTO.main(message, False)
        return render_template('zeroarg.html', title=name,   crypto=crypto,   key=key,    decrypto=decrypto)


@app.route('/A52', methods=['POST', 'GET'])
def A52():
    import A5_second as CRYPTO
    name='A5/2'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto, decrypto, key = CRYPTO.main(message, False)
        return render_template('zeroarg.html', title=name,   crypto=crypto,   key=key,    decrypto=decrypto)

@app.route('/magma', methods=['POST', 'GET'])
def magma():
    import magma as CRYPTO
    name='МАГМА'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name, magma=True)
    if (request.method=='POST'):
        message = request.form.get('message')
        mode = request.form.get('mode')
        print(mode)
        if mode == '3':
            imito = CRYPTO.main(message, False, mode)
            return render_template('zeroarg.html', title=name, magma=True,  imito=imito)
        else:
            crypto, decrypto = CRYPTO.main(message, False, mode)
            return render_template('zeroarg.html', title=name, magma=True,  crypto=crypto, decrypto=decrypto)


@app.route('/rsa', methods=['POST', 'GET'])
def rsa():
    import RSA as CRYPTO
    name='RSA'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto, decrypto, RSAkey = CRYPTO.main(message, False, 1)
        return render_template('zeroarg.html', title=name, crypto=crypto, decrypto=decrypto, RSAkey=RSAkey)


@app.route('/elgamal', methods=['POST', 'GET'])
def elgamal():
    import elgamal as CRYPTO
    name='elgamal'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        crypto, decrypto, RSAkey = CRYPTO.main(message, False, 0)
        return render_template('zeroarg.html', title=name, crypto=crypto, decrypto=decrypto, RSAkey=RSAkey)


@app.route('/rsaECP', methods=['POST', 'GET'])
def rsaECP():
    import RSAECP as CRYPTO
    name='RSA ЭЦП'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        ECP, RSAkey = CRYPTO.main(message, False, 1)
        return render_template('zeroarg.html', title=name, ECP=ECP, RSAkey=RSAkey)

@app.route('/elgamalECP', methods=['POST', 'GET'])
def elgamalECP():
    import elgamalECP as CRYPTO
    name='elgamal ЭЦП'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        ECP, RSAkey = CRYPTO.main(message, False, 0)
        return render_template('zeroarg.html', title=name, ECP=ECP, RSAkey=RSAkey)

@app.route('/gost94', methods=['POST', 'GET'])
def gost94():
    import GOST94 as CRYPTO
    name='elgamal ЭЦП'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        ECP, key94 = CRYPTO.main(message, False, 0)
        return render_template('zeroarg.html', title=name, ECP=ECP, key94=key94)

@app.route('/gost2012', methods=['POST', 'GET'])
def gost2012():
    import GOST2012 as CRYPTO
    name='ГОСТ Р 34.10-2012'
    if (request.method=='GET'):
        return render_template('zeroarg.html', title=name)
    if (request.method=='POST'):
        message = request.form.get('message')
        ECP, key2012 = CRYPTO.main(message, False, 0)
        return render_template('zeroarg.html', title=name, ECP=ECP, key2012=key2012)

@app.route('/diffihellman', methods=['POST', 'GET'])
def diffihellman():
    import PZ11 as CRYPTO
    name='Обмен ключами'
    if (request.method=='GET'):
        return render_template('DH.html', title=name)
    if (request.method=='POST'):
        n = int(request.form.get('N'))
        a = int(request.form.get('A'))
        ka = int(request.form.get('ka'))
        kb = int(request.form.get('kb'))
        DH = CRYPTO.main(n,a,ka,kb)
        return render_template('DH.html', title=name, DH=DH)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=800)