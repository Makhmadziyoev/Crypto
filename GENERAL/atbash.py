# АТБАШ
# arr1 = [chr(x) for x in range(65, 91)]
# arr2 = [x for x in arr1]
# arr2.reverse()

alfRU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
print(len(alfRU))

arr2 = [x for x in alfRU]
arr2.reverse()

print(alfRU)
print(arr2)
text = "КАЖДАЯКЛАДКАДОЛЖНАСТОЯТЬНАСОБСТВЕННОМДНИЩЕТЧК"

encrypt = ""
for i in text:
    for j, l in enumerate(alfRU):
        if i == l:
            encrypt += arr2[j]

print(encrypt)

decrypt = ""
for i in encrypt:
    for j, l in enumerate(arr2):
        if i == l:
            decrypt += alfRU[j]
print(decrypt)


