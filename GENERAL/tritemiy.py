# Шифр Тритемия
# Выбираем Шифрование или Расшифрование
cryptMode = input("Шифровать или Расшифровать? ")
if cryptMode not in ['Ш', 'Р']:
    print("Ошибка! Введите Ш(шифровать) или Р(расшифровать)"); raise SystemExit

# Вводим наше сообщение, так же убираю символы которых нет в алфавите
startMessage = list(input("Введите сообщение: ").upper())
for symbol in startMessage:
    if symbol not in [chr(x) for x in range(1040, 1072)]:
        startMessage.remove(symbol)
funcKey = lambda x: x+1

# Функция шифрования и Расшифрования
def EncryptDectypt(mode, message, key, final = ""):
    for index, symbol in enumerate(message):
        if mode == "Ш":
            temp = ord(symbol) + key(index) - 17
        else:
            temp = ord(symbol) - key(index) + 17
        final += chr(temp%32 + ord("А"))
    return final


print(EncryptDectypt(cryptMode, startMessage, funcKey))

