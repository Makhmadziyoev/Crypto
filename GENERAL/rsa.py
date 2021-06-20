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

# количество цифр в числе
def sflex(number):
	return len(str(number))

# вычисление d
def find_d_point(a,b,m):
	fim=ayler(m)
	x=(a**(fim-1))%m
	return x

# заполнение массива чисел для введенного текста
def piezone(string,dic):
	return [creamthepie(dic,i) for i in string]

# заполнение массива чисел зашифрованного текста
def creamzone(string, u):
	numarray=[]
	for i in range(0,len(string),u):
		checkZero=0
		str_num=""
		for j in range(u):
			if int(string[i+j])>0 and checkZero==0:
				str_num+=string[i+j]
				checkZero=1
			elif int(string[i+j])>=0 and checkZero>0:
				str_num+=string[i+j]
		numarray.append(int(str_num))
	return numarray

# тестовая функция для проверки значений
# def testcream(origpie,dic,idic,e,u,v):
# 	print("\n")
# 	zeros=[]
# 	for x in range(len(dic)):
# 		zeros.append(int(0))
# 	for i in origpie:
# 		if zeros[i-1]==0:
# 			y=(i**e)%v
# 			print(creamthepie(idic,i)," = (",i," ** ",e,") mod ",v," = ", y)
# 			zeros[i-1]+=1
# 	exit()

def encrypt(array,e,u,v):
	enc=""
	for x in array:
		y=(x**e)%v
		if sflex(y)<u:
			k=u-sflex(y)
			while k>0:
				enc+="0"
				k-=1
			enc+=str(y)
		elif sflex(y)==u:
			enc+=str(y)
	return enc

def decrypt(array,idic,d,v):
	dec=""
	for x in array:
		y=(x**d)%v
		dec+=creamthepie(idic,y)
	return dec

# свой алфавит из 32 символов
dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32}
idic=lickthecream(dic)

p=int(input("\nВведите p: "))
# p=59
if ayler(p)!=p-1:
	print('\nОшибка. p - простое число.\n')
	exit()
q=int(input("Введите q: "))
# q=71
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
finflex=sflex(n)
e=int(input("\nВведите e: "))
# e=303
if euclid(e,fin)!=1:
	print('\nОшибка. e - взаимно простое с fi(n).\n')
	exit()
print("\nОткрытые ключи:\nn: ",n,"\ne: ", e)
d=find_d_point(e,1,fin)
print("\nСекретный ключ d:", d)

# orig="этакапустазеленаязптвсеравночтоэтозеленаякапустатчк"
# origpie=piezone(orig,dic)
# testcream(origpie,dic,idic,e,finflex,n)
# cry=encrypt(origpie,e,finflex,n)
# print("\nЗашифрованный текст: ", cry)
# print("\n")
# print(decrypt(creamzone(cry,finflex),idic,d,n))


ask=input("\nЗашифровать? (д/н): ")
if ask=='д':
	orig=input("\nВведите исходный текст: ")
	origpie=piezone(orig,dic)
	cry=encrypt(origpie,e,finflex,n)
	print("\nЗашифрованный текст: ", cry)

elif ask=='н':
	orig=input("\nВведите зашифрованный текст: ")
	if len(orig)%finflex!=0:
		print("Ошибка. Длина шифртекста не кратна количесту цифр в n.")
		exit()
	origcz=creamzone(orig,finflex)
	cry=decrypt(origcz,idic,d,n)
	print("\nРасшифрованный текст: ", cry)

else:
	print('\nОшибка. Повторите с требуемым ответом.\n')
	exit()