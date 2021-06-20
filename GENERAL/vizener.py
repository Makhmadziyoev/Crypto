# Шифр Виженера
# Шифрование

m = "КАЖДАЯКЛАДКАДОЛЖНАСТОЯТЬНАСОБСТВЕННОМДНИЩЕТЧК"
k = "В"
k2 = k + m
k2 = k2[:-1]
c = ""
print("Ключ: ",k)
for i, j in enumerate(m):
    gg = (ord(j) + ord(k2[i]))
    c += chr(gg%32 + ord("А"))
print("Зашифрованное сообщение: "+str(c))

# Расшифрование

c1 = c
k3 = k2
d = ""
for i, j in enumerate(c1):
    gg = (ord(j) - ord(k2[i]))
    d += chr(gg%32 + ord("А"))
print("Расшифрованное сообщение: ", str(d))