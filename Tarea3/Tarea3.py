import camellia

c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_OFB)
c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_OFB)

msg="Mensaje en texto plano "
print("Mensaje en texto plano:", msg)

encript=c1.encrypt(msg.encode("utf-8"))
print("Mensaje encriptado:",encript.hex())

decript=c2.decrypt(encript)
print("Mensaje desencriptado:",decript.decode("utf-8"))

html=open("output.html","w")
html.write(''' 
    <html>
        <head></head>
        <title>Pagina generada por python</title>
        <body>
            <p>Esta pagina contiene un mensaje secreto</p>
            <div class="Camellia" id= "%s" >
            </div>
        </body>
    </html>
        ''' % encript.hex())
html.close()


