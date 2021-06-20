def creamthepie(d, value):
    for k, v in d.items():
        if v == value:
            return k

Ti = int(input('\nВведите Т0: '))
a = int(input('Введите a: '))
c = int(input('Введите c: '))
m = 33
mystr = input('Введите фразу: ')
strList = [x for x in mystr]
print('\nДлина фразы: ', len(mystr), '\n')

dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}
dicZero = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31}
dicZero33 = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}

keyList = list()
# keyList.append(Ti)

# i = 1
i = 0
while i < len(mystr):
    Ti = (a * Ti + c) % m
    keyList.append(Ti)
    i += 1
# print('\n')
print('Гамма: \n', keyList)
print('\n')

newList = list()
for i in range (len(mystr)):
    newList.append(dicZero33[strList[i]])


endListEncrypt = list()
for i in range (len(mystr)):
    n = (keyList[i] + newList[i]) % m
    creamthepie(dicZero33, n)
    endListEncrypt.append(creamthepie(dicZero33, n))

endListDecrypt = list()
for i in range (len(mystr)):
    n = (newList[i] - keyList[i])
    if n < 0:
        n += m
    creamthepie(dicZero33, n)
    endListDecrypt.append(creamthepie(dicZero33, n))


print('Зашифрованный текст: ', ''.join(endListEncrypt))
print('\nДлина зашифрованного текста: ', len(endListEncrypt), '\n')
print('Расшифрованный текст: ', ''.join(endListDecrypt))
print('\nДлина расшифрованного текста: ', len(endListDecrypt), '\n')

