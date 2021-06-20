# Шифр Белазо


m = "КАЖДАЯКЛАДКАДОЛЖНАСТОЯТЬНАСОБСТВЕННОМДНИЩЕТЧК"
k = "ГТА"
print("Ключ:", k)
k *= len(m)//len(k)+1
c = ""
for i, j in enumerate(m):
    gg = (ord(j)+ord(k[i]))
    c += chr(gg%32 + ord("А"))
print("Зашифрованное сообщение: "+str(c))

# Расшифрование

c1 = c
k2 = k
d = ""
for i, j in enumerate(c1):
    gg = (ord(j)-ord(k[i]))
    d += chr(gg%32+ord("А"))
print("Расшифрованное сообщение: ", str(d))





