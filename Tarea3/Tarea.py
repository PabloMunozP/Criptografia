from Crypto.Cipher import DES
key = b'Secretos'
cipher = DES.new(key, DES.MODE_CFB)
plaintext = b'Texto plano'
msg = cipher.iv + cipher.encrypt(plaintext)

print(msg.hex())

html=open("output.html","w")
html.write(''' 
    <html>
        <head></head>
        <title>Pagina generada por python</title>
        <body>
            <p>Esta pagina contiene un mensaje secreto</p>
            <div class="DES" id= "%s" > Texto</div>
        </body>
    </html>
        ''' % msg.hex())
html.close()