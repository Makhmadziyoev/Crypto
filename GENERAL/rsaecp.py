# получение порядка буквы по словарю
def creamthepie(d, value):
    if value in d:
    	return d[value]
    else:
    	print(value, " нет в словаре.")
    	exit()

# инверсия словаря
def lickthecream(d):
	h={}
	for k,v in d.items():
		h[v]=k
	return h

dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}
# dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14, 'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19, 'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24, 'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29, 'ю': 30, 'я': 31}
idic=lickthecream(dic)


# функция Эйлера
def ayler(n):
    f = n;
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i;
            f = f // i;
            f = f * (i-1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n-1);
    return f;

# алгоритм Евклида
def euclid(a,b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a

# хэш:
def hash(text):
    h = []
    i=0
    h.append(int(0))
    for char in text:
        # print('h[',i,'] =',h[i])
        # print('h[',i+1,'] = (h[',i,'] + ',dic[char],')^2 mod ',n,' = ', ((h[-1]+dic[char])**2) % n,'\n')
        # print("\n")
        h.append(((h[-1]+dic[char])**2) % n)
        i+=1

    print('\nХэш:', h[-1],"\n")
    return h[-1]


p=int(input("\nВведите p: "))
# p=31
if ayler(p)!=p-1:
    print('\nОшибка. p - простое число.\n')
    exit()
q=int(input("Введите q: "))
# q=37
if ayler(q)!=q-1:
    print('\nОшибка. q - простое число.\n')
    exit()
n=p*q
if(n<len(dic)):
    print('\nОшибка. Слишком малые значение p и q.\n')
    exit()
print("n = p * q = ", n)
fin=ayler(n)
print("fi(n) = ", fin)
e=int(input("\nВведите e: "))
# e=23
if euclid(e,fin)!=1:
    print('\nОшибка. e - взаимно простое с fi(n).\n')
    exit()
print("\nОткрытые ключи:\nn: ",n,"\ne: ", e)
d = e ** (fin - 1) % fin
print("\nСекретный ключ d:", d)

# orig="этакапустазеленаязптвсеравночтоэтозеленаякапустатчк"
# hm=hash(orig)
# sign=(hm**d)%n
# print("Подпись: ", sign)
# mate=(sign**e)%n
# if mate==hm:
#     print("Подпись верна")
# else:
#     print("Подпись неверна")
# exit()

ask=input("\nСгенерировать подпись? (д/н): ")
if ask=='д':
    orig=input("\nВведите исходный текст: ")
    # print("\n")
    hm=hash(orig)
    sign=(hm**d)%n
    print("Подпись: ", sign)

elif ask=='н':
    orig=input("\nВведите исходный текст: ")
    hm=hash(orig)
    sign=int(input("\nВведите подпись: "))
    mate=(sign**e)%n
    if mate==hm:
        print("Подпись верна")
    else:
        print("Подпись неверна")

else:
    print('\nОшибка. Повторите с требуемым ответом.\n')
    exit()