#Шифр Цезаря
alfRU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
print(len(alfRU))

arr2=[]
for i in range(len(alfRU)):
	arr2.append(alfRU[i])


def change_arr2():
	for i in range(number):
		arr2.append(arr2[0])
		arr2.remove(arr2[0])

number=int(input("[*] Введите ключ [0-%s]: " % (str(len(alfRU)))))

change_arr2()
# Шифрование

#msg=input("\n[*] Write the text:\n[text] >> ")
text = "КАЖДАЯКЛАДКАДОЛЖНАСТОЯТЬНАСОБВСТВЕННОМДНИЩЕТЧК"
crypt= ""
for i in text:
    for j in range(len(alfRU)):
        if i==alfRU[j]:
            crypt+=arr2[j]
# print(alfRU)
print(crypt)

# Расшифрование

decrypt= ""

for i in crypt:
	for j in range(len(alfRU)):
		if i == arr2[j]:
			decrypt += alfRU[j]
print(decrypt)